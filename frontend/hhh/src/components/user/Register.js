import React from "react";
import axios from "axios";
import { useHistory } from "react-router-dom";
import { Form, Input, Select, Row, Col, Button } from "antd";
import "./Register.scss";
import Profile from "./Profile";

const { Option } = Select;
const registerUrl = `http://13.125.113.171:8000/users/`;

const formItemLayout = {
  labelCol: {
    xs: {
      span: 24,
    },
    sm: {
      span: 8,
    },
  },
  wrapperCol: {
    xs: {
      span: 16,
    },
    sm: {
      span: 8,
    },
  },
};
const tailFormItemLayout = {
  wrapperCol: {
    xs: {
      span: 24,
      offset: 0,
    },
    sm: {
      span: 16,
      offset: 8,
    },
  },
};

function onChange(value) {
  console.log(`selected ${value}`);
}

const Register = () => {
  const [form] = Form.useForm();
  let history = useHistory();

  const onFinish = async (values) => {
    console.log(values);
    await axios.post(registerUrl, values).then((resp) => {
      if (resp.status === 201) {
        sessionStorage.setItem("username", values.username);
        history.push("/");
      }
    });
  };

  return (
    <div className="registerContainer">
      <Form
        {...formItemLayout}
        form={form}
        name="register"
        onFinish={onFinish}
        scrollToFirstError
      >
        <Form.Item
          name="username"
          label={<span>아이디&nbsp;</span>}
          rules={[
            {
              required: true,
              message: "아이디를 입력해주세요!",
              whitespace: true,
            },
          ]}
        >
          <Input />
        </Form.Item>
        <Form.Item
          name="password"
          label="비밀번호"
          rules={[
            {
              required: true,
              message: "비밀번호를 입력해주세요!",
            },
          ]}
          hasFeedback
        >
          <Input.Password />
        </Form.Item>
        <Form.Item
          name="confirm"
          label="비밀번호 확인"
          dependencies={["password"]}
          hasFeedback
          rules={[
            {
              required: true,
              message: "비밀번호를 다시 입력해주세요!",
            },
            ({ getFieldValue }) => ({
              validator(rule, value) {
                if (!value || getFieldValue("password") === value) {
                  return Promise.resolve();
                }

                return Promise.reject("비밀번호가 맞지 않아요!");
              },
            }),
          ]}
        >
          <Input.Password />
        </Form.Item>
        <Form.Item
          name="email"
          label="이메일"
          rules={[
            {
              type: "email",
              message: "이메일의 형식이 맞지 않아요!",
            },
            {
              required: true,
              message: "이메일을 입력해주세요.",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item name="gender" label="성별">
          <Select
            showSearch
            style={{ width: 200 }}
            onChange={onChange}
            filterOption={(input, option) =>
              option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
            }
            defaultValue="none"
          >
            <Option value="male">Male</Option>
            <Option value="female">Female</Option>
            <Option value="none">None</Option>
          </Select>
        </Form.Item>

        <Form.Item {...tailFormItemLayout}>
          <Button type="primary" htmlType="submit">
            회원가입
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Register;
