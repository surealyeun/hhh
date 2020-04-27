import React, { Component } from "react";
import axios from "axios";
import { Form, Input, Button } from "antd";

import "antd/dist/antd.css";
import "./userInfo.scss";

const userID = sessionStorage.getItem("username");
const userUrl = `http://13.125.113.171:8000/users/detail/${userID}/`;
const updateUrl = `http://13.125.113.171:8000/users/update/delete/${userID}/`; // username, password 필수로 입력해줘야 함

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 8,
  },
};

const tailLayout = {
  wrapperCol: {
    offset: 9,
    span: 16,
  },
};

class userInfo extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {},
      username: "",
      password: "",
      first_name: "",
      last_name: "",
      email: "",
      avatar: null,
      imagePreviewUrl: "",
    };
  }

  async componentDidMount() {
    let { data: user } = await axios.get(userUrl);
    this.setState({ user });
    this.setState({
      username: this.state.user.username,
      password: this.state.user.password,
      first_name: this.state.user.first_name,
      last_name: this.state.user.last_name,
      email: this.state.user.email,
      avatar: this.state.user.avatar,
    });
  }

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleAvatarChange = (e) => {
    let reader = new FileReader();
    let file = e.target.files[0];
    reader.onloadend = () => {
      this.setState({ avatar: file, imagePreviewUrl: reader.result });
    };
    reader.readAsDataURL(file);
  };

  handleSubmit = (e) => {
    e.preventDefault();
    let form_data = new FormData();
    form_data.append("avatar", this.state.avatar, this.state.avatar.name);
    form_data.append("username", this.state.username);
    form_data.append("password", this.state.password);
    form_data.append("first_name", this.state.first_name);
    form_data.append("last_name", this.state.last_name);
    form_data.append("email", this.state.email);

    axios
      .put(updateUrl, form_data, {
        headers: {
          "content-type": "multipart/form-data",
        },
      })
      .then((response) => console.timeLog(response))
      .catch((err) => console.timeLog(err));
  };

  render() {
    let { imagePreviewUrl } = this.state;
    let $imagePreview = null;
    return (
      <div className="userInfoContainer">
        {!$imagePreview && <img src={imagePreviewUrl ? imagePreviewUrl : `http://13.125.113.171:8000` + this.state.avatar} />}
        <br />
        <input
          type="file"
          id="image"
          accept="image/png, image/jpeg"
          onChange={this.handleAvatarChange}
          required
        />
        <Form {...layout} onSubmitCapture={this.handleSubmit}>
          <Form.Item name="username" label="아이디">
            <Input
              name="username"
              value={this.state.username}
              placeholder={this.state.username}
              disabled
            />
          </Form.Item>
          <Form.Item label="이름" style={{ marginBottom: 0 }}>
            <Form.Item
              name="first_name"
              style={{ display: "inline-block", width: "calc(50% - 8px)" }}
            >
              <Input
                name="first_name"
                value={this.state.first_name}
                placeholder={this.state.first_name}
                onChange={this.handleChange}
              />
            </Form.Item>
            <Form.Item
              name="last_name"
              style={{
                display: "inline-block",
                width: "calc(50% - 8px)",
                margin: "0 8px",
              }}
            >
              <Input
                name="last_name"
                value={this.state.last_name}
                placeholder={this.state.last_name}
                onChange={this.handleChange}
              />
            </Form.Item>
          </Form.Item>
          <Form.Item label="이메일" name="email">
            <Input
              name="email"
              value={this.state.email}
              placeholder={this.state.email}
              onChange={this.handleChange}
            />
          </Form.Item>
          <Form.Item className="submitButton" {...tailLayout}>
            <Button type="primary" htmlType="submit">
              수정
            </Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

export default userInfo;
