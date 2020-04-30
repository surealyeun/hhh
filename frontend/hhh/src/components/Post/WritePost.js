import React from "react";
import { Redirect } from "react-router-dom";
import { Form, Upload, Modal, Input, Button, Rate } from "antd";
import { PlusOutlined, EnvironmentTwoTone } from "@ant-design/icons";
import "./WritePost.scss";
import axios from "axios";
import Header from "../common/Header";

const URL = "http://13.125.113.171:8000/";
const postURL = `http://13.125.113.171:8000/boards/`;
const username = sessionStorage.getItem("username");

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
    isWrite: false,
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
    if (this.state.isWrite) {
      return <Redirect to={{ pathname: `/store/${this.props.location.state.id}`}} />;
    }
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
    const place = isStore ? "store" : "location";

    const onFinish = (values) => {
      console.log(values);
      let form_data = new FormData();
      form_data.append("address_gu", state.area);
      form_data.append("writer", sessionStorage.getItem("userId"));
      form_data.append("content", values.content);
      if (isStore) {
        form_data.append("store", state.id);
      } else {
        form_data.append("location", state.id);
      }

      for (let index = 0; index < fileList.length; index++) {
        if (index === 0) {
          form_data.append("photo", this.state.fileList[0].originFileObj);
        } else {
          form_data.append(
            `photo${index + 1}`,
            this.state.fileList[index].originFileObj
          );
        }
      }
      axios
        .post(postURL, form_data, {
          headers: {
            "content-type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);
          this.setState({ isWrite: true });
        })
        .catch((err) => console.timeLog(err));

      axios
        .post(
          `${URL}wishlist/${place}/${this.props.location.state.id}/${username}/${values.rate}`
        )
        .then((resp) => console.log(resp));
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
                  {fileList.length >= 3 ? null : uploadButton}
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
