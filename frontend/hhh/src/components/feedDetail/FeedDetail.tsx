import React, { Component } from "react";
import axios from "axios";
import Header from "../common/Header";
import { HeartOutlined, HeartFilled } from "@ant-design/icons";
import "./FeedDetail.scss";

export interface Comment {
  created?: number[];
  updated?: number[];
  id?: number;
  text: string;
  writer_id?: number;
  board_id?: number;
  parents_id?: any;
  username: string;
  avatar: string;
}

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
    loginAvatar: sessionStorage.getItem("avatar"),
    isLike: false,
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

    await axios
      .get("http://13.125.113.171:8000/feedlist/follow/" + this.state.loginUser)
      .then((res) => {
        console.log(res.data);

        for (let index = 0; index < res.data.length; index++) {
          const element = res.data[index];

          if (element.id === Number(this.state.feedid)) {
            this.setState({
              isLike: element.pressLike,
            });
          }
        }
      });
  }

  addComment = () => {
    if (this.state.loginUserId === null) {
      alert("로그인 해주세요");
      return;
    }

    const url: string = "http://13.125.113.171:8000";
    const avatarr: string | null = url + sessionStorage.getItem("avatar");
    const userName: string | null = sessionStorage.getItem("username");
    axios
      .post(
        "http://13.125.113.171:8000/comment/post/" +
          this.state.feedid +
          "/" +
          this.state.loginUserId +
          "/" +
          this.state.text
      )
      .then((res) => {
        console.log(res);

        if (userName !== null) {
          let newComments: any = this.state.comments;

          let newComment: Comment = {
            text: this.state.text,
            username: userName,
            avatar: avatarr,
          };

          newComments.push(newComment);
          this.setState({
            comments: newComments,
          });
        }

        this.setState({
          text: "",
        });
      });
  };

  toggleLike = () => {
    if (this.state.isLike) {
      // cancle like
      console.log("delete");
      this.setState({
        likes: this.state.likes - 1,
        isLike: !this.state.isLike,
      });
      axios({
        method: "delete",
        url:
          "http://13.125.113.171:8000/board/like/delete/" +
          this.state.loginUser +
          "/" +
          this.state.loginUserId,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log("fail delete like", err);
        });
    } else {
      // like
      console.log("like");
      this.setState({
        likes: this.state.likes + 1,
        isLike: !this.state.isLike,
      });
      axios({
        method: "post",
        url:
          "http://13.125.113.171:8000/board/like/post/" +
          this.state.loginUser +
          "/" +
          this.state.loginUserId,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log("fail like", err);
        });
    }
  };

  render() {
    return (
      <>
        <Header />
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
            <div id="feed-btns" onClick={this.toggleLike}>
              {this.state.isLike ? <HeartFilled /> : <HeartOutlined />}
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
                onChange={(e) => this.setState({ text: e.target.value })}
                value={this.state.text}
              />
              <div id="make" onClick={this.addComment}>
                게시
              </div>
            </div>
          </div>
        </div>
      </>
    );
  }
}

export default FeedDetail;
