import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { Form, Input, Button, Checkbox } from "antd";
import "./Login.scss";
import axios from "axios";

const loginURL = `http://192.168.219.105:8080/login/`;

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
    offset: 14,
    span: 16,
  },
};

const Login = () => {
  let history = useHistory();

  const onFinish = async (values) => {
    const resultURL = loginURL + `${values.username}/${values.password}`;
    await axios
      .get(resultURL, {
        username: values.username,
        password: values.password,
      })
      .then((resp) => {
        console.log(resp);
        if (resp.status === 200) {
          sessionStorage.setItem("username", values.username);
          history.push("/");
        }
      });
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <div className="loginContainer">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ7ly6Nep4C_fGpdCTAxzjDeyNhLUsRWrdqdg_tbvey6WxsYgzs&usqp=CAU" />
      <Form
        {...layout}
        name="basic"
        initialValues={{
          remember: true,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[
            {
              required: true,
              message: "Please input your username!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[
            {
              required: true,
              message: "Please input your password!",
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item {...tailLayout} name="remember" valuePropName="checked">
          <Checkbox>로그인 유지하기</Checkbox>
        </Form.Item>

        <Form.Item {...tailLayout}>
          <Button type="primary" htmlType="submit">
            로그인
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Login;
