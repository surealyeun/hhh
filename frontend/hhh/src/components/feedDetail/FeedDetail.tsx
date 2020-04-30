import React, { Component } from "react";
import axios from "axios";

import { HeartOutlined, HeartFilled } from "@ant-design/icons";
import "./FeedDetail.scss";

class FeedDetail extends Component {
  state = {
    avatar: "",
    userName: "",
    photos: [],
    content: "",
    likes: 0,
    comments: [],
    feedid: window.location.href.split("/")[4],
    text: "",
    loginUserId: sessionStorage.getItem("userId"),
    loginUser: sessionStorage.getItem("username"),
  };

  async componentDidMount() {
    let writer = 0;

    await axios
      .get("http://13.125.113.171:8000/boards/" + this.state.feedid)
      .then((res) => {
        console.log(res.data);
        this.setState({
          content: res.data.content,
        });
        writer = res.data.writer;
      });

    await axios
      .get("http://13.125.113.171:8000/users/" + writer)
      .then((res) => {
        console.log(res.data);
        this.setState({
          avatar: res.data.avatar,
          userName: res.data.username,
        });
      });

    await axios({
      method: "get",
      url: "http://13.125.113.171:8000/feedlist/follow/" + this.state.userName,
    }).then((res) => {
      console.log(res.data);
      for (let index = 0; index < res.data.length; index++) {
        const element = res.data[index];

        if (element.id === Number(this.state.feedid)) {
          this.setState({
            photos: element.photos,
            comments: element.comments,
            likes: element.likes,
          });

          break;
        }
      }
    });
  }

  addComment = () => {
    axios
      .post(
        "http://13.125.113.171:8000/comment/post/" +
          this.state.loginUser +
          "/" +
          this.state.loginUserId
      )
      .then((res) => {
        console.log(res);
      });
  };

  render() {
    return (
      <div id="feed-detail">
        <div id="user-id">
          <img className="user-pic" src={this.state.avatar} alt="" />
          <div id="id">{this.state.userName}</div>
        </div>

        <div id="feed-img">
          <img src={this.state.photos[0]} alt=""></img>
        </div>

        <div id="feed-inside">
          <div id="content">{this.state.content}</div>
          <div id="feed-btns">
            <HeartOutlined></HeartOutlined>
          </div>
          <div id="likes">좋아요 {this.state.likes}개</div>
          <div id="feed-text">
            <ul>
              {this.state.comments.map((comment: any) => (
                <li key={comment.id}>
                  <img src={comment.avatar} alt="" />
                  <div className="id">{comment.username}</div>
                  <div className="text">{comment.text}</div>
                </li>
              ))}
            </ul>
          </div>

          <div id="make-text">
            <input
              type="text"
              placeholder="댓글 달기..."
              value={this.state.text}
            />
            <div id="make">게시</div>
          </div>
        </div>
      </div>
    );
  }
}

export default FeedDetail;
