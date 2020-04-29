import React from "react";
import { Form, Upload, Modal, Input, Button, Rate } from "antd";
import { PlusOutlined, EnvironmentTwoTone } from "@ant-design/icons";
import "./WritePost.scss";
import axios from "axios";
import Header from "../common/Header";

const postURL = `http://13.125.113.171:8000/board/post`;

const { TextArea } = Input;
function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = (error) => reject(error);
  });
}

class PicturesWall extends React.Component {
  state = {
    previewVisible: false,
    previewImage: "",
    previewTitle: "",
    fileList: [],
  };

  handleCancel = () => this.setState({ previewVisible: false });

  handlePreview = async (file) => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj);
    }

    this.setState({
      previewImage: file.url || file.preview,
      previewVisible: true,
      previewTitle:
        file.name || file.url.substring(file.url.lastIndexOf("/") + 1),
    });
  };

  handleChange = ({ fileList }) => this.setState({ fileList });

  render() {
    const { previewVisible, previewImage, fileList, previewTitle } = this.state;
    const uploadButton = (
      <div>
        <PlusOutlined />
        <div className="ant-upload-text">Upload</div>
      </div>
    );
    const state = this.props.location.state;
    const isStore = state.isStore;
    const placeName = isStore ? state.store_name : state.location_name;
    const onFinish = (values) => {
      let form_data = new FormData();
      form_data.append("content", values.content);
      form_data.append("writer", sessionStorage.getItem("userId"));
      // form_data.append("rate", values.rate); // 별점 컬럼 생성 시 추가
      if (isStore) {
        form_data.append("store", this.props.location.state.id);
      } else {
        form_data.append("location", this.props.location.state.id);
      }
      // 여기 고민...
      for (let index = 0; index < fileList.length; index++) {
        form_data.append("photo", fileList[index]);
      }
      axios
        .post(postURL, form_data, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((response) => console.timeLog(response))
        .catch((err) => console.timeLog(err));
    };
    return (
      <>
        <Header />
        <br />
        <div className="writeContainer">
          <Form name="validate_other" onFinish={onFinish}>
            <div className="position">
              <h3>
                <EnvironmentTwoTone /> {placeName}
              </h3>
              <Form.Item name="rate">
                <Rate className="rate" />
              </Form.Item>
              <hr />
              <br />
            </div>
            <div className="clearfix">
              <Form.Item name="photo">
                <Upload
                  action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
                  listType="picture-card"
                  fileList={fileList}
                  onPreview={this.handlePreview}
                  onChange={this.handleChange}
                >
                  {fileList.length >= 10 ? null : uploadButton}
                </Upload>
              </Form.Item>
              <Modal
                visible={previewVisible}
                title={previewTitle}
                footer={null}
                onCancel={this.handleCancel}
              >
                <img
                  alt="example"
                  style={{ width: "100%" }}
                  src={previewImage}
                />
              </Modal>
            </div>
            <div className="writeSpace">
              <Form.Item name="content">
                <TextArea rows={9} />
              </Form.Item>
            </div>
            <br />
            <Form.Item>
              <Button htmlType="submit">작성완료</Button>
            </Form.Item>
          </Form>
        </div>
      </>
    );
  }
}

export default PicturesWall;
