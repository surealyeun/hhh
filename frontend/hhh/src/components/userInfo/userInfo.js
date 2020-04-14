import React, { Component } from "react";
import axios from "axios";
import { Form, Input, Button, Row, Col, Select, Upload } from "antd";
import { Avatar } from "antd";
import { UploadOutlined, UserOutlined } from "@ant-design/icons";

import "antd/dist/antd.css";
import "./userInfo.scss";

const userUrl = `http://13.125.113.171:8000/users/detail/joker/`;

const { Option } = Select;

const layout = {
  labelCol: {
    span: 8,
  },
  wrapperCol: {
    span: 16,
  },
};

const tailLayout = {
  wrapperCol: {
    offset: 8,
    span: 16,
  },
};

class userInfo extends Component {
  constructor(props) {
    super(props);
    this.state = { user: {} };
  }

  async componentDidMount() {
    let { data: user } = await axios.get(userUrl);
    this.setState({ user });
  }

  render() {
    const { user } = this.state;

    return (
      <div className="userInfoContainer">
        <Row>
          <Col span={12} offset={6}>
            <Form
              {...layout}
              name="basic"
              initialValues={{
                remember: true,
              }}
            >
              <Avatar
                className="userAvatar"
                size={64}
                icon={<UserOutlined />}
              />
              <Form.Item
                name="upload"
                label="Profile Image"
                valuePropName="fileList"
              >
                <Upload name="logo" action="/upload.do" listType="picture">
                  <Button>
                    <UploadOutlined /> Click to upload
                  </Button>
                </Upload>
              </Form.Item>
              <Form.Item label="Username" name="username">
                <Input style={{ width: "70%" }} placeholder={user.username} />
              </Form.Item>

              <Form.Item label="Password" name="password">
                <Input.Password style={{ width: "70%" }} />
              </Form.Item>

              <Form.Item name="gender" label="Gender">
                <Select
                  style={{ width: "70%" }}
                  placeholder={user.gender}
                  allowClear
                >
                  <Option value="male">male</Option>
                  <Option value="female">female</Option>
                  <Option value="other">other</Option>
                </Select>
              </Form.Item>

              <Form.Item className="submitButton" {...tailLayout}>
                <Button type="primary" htmlType="submit">
                  수정
                </Button>
                &nbsp;&nbsp;
                <Button type="danger" htmlType="submit">
                  회원탈퇴
                </Button>
              </Form.Item>
            </Form>
          </Col>
        </Row>
      </div>
    );
  }
}

export default userInfo;
