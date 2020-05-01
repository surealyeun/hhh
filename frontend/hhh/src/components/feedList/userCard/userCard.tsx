import React from "react";
import { Link } from "react-router-dom";
import "./userCard.scss";
import axios from "axios";

class UserCard extends React.Component<{
  avatarPic: string;
  userId: number;
  feedNum: number;
}> {
  state = {
    username: window.location.href.split("/")[4],
    userId: this.props.userId,
    followerNum: 0,
    followingNum: 0,
    same: false,
    loginUserId: sessionStorage.getItem("id"),
    isFollow: false,
  };

  async componentDidUpdate(prevProps: any) {
    if (this.props.userId !== prevProps.userId) {
      if (sessionStorage.getItem("username") === this.state.username) {
        this.setState({
          same: true,
        });
      }

      sessionStorage.setItem("originUserName", this.state.username);

      await axios
        .get("http://13.125.113.171:8000/following/" + this.state.loginUserId)
        .then((res) => {
          for (let index = 0; index < res.data.length; index++) {
            const element = res.data[index];
            if (element.id === this.props.userId) {
              // 팔로우가 된 상태
              this.setState({
                isFollow: true,
              });

              break;
            }
          }
        });

      await axios
        .get("http://13.125.113.171:8000/follower/" + this.props.userId)
        .then((res) => {
          this.setState({
            userId: this.props.userId,
            followerNum: res.data.length,
          });
        });

      await axios
        .get("http://13.125.113.171:8000/following/" + this.props.userId)
        .then((res) => {
          this.setState({ followingNum: res.data.length });
        });
    }
  }

  toggleFollow = () => {
    if (this.state.isFollow) {
      // 팔로우가 된 상태
      axios
        .delete(
          "http://13.125.113.171:8000/unfollow/" +
            this.state.loginUserId +
            "/" +
            this.props.userId
        )
        .then((res) => {
          this.setState({
            isFollow: false,
            followerNum: this.state.followerNum - 1,
          });
        });
    } else {
      // 팔로우가 안 된 상태
      if (this.state.loginUserId !== null) {
        // 로그인된 상태
        axios
          .post(
            "http://13.125.113.171:8000/follow/" +
              this.state.loginUserId +
              "/" +
              this.props.userId
          )
          .then((res) => {
            this.setState({
              isFollow: true,
              followerNum: this.state.followerNum + 1,
            });
          });
      } else {
        // 로그인이 안 된 상태
        alert("로그인이 필요합니다.");
      }
    }
  };

  render() {
    return (
      <div id="user-card">
        <div id="avatar">
          <img src={this.props.avatarPic} alt="" />
        </div>
        <div id="user-info">
          <div id="user-id">{this.state.username}</div>
          <div
            id="follow-btn"
            style={
              this.state.same
                ? { display: "none" }
                : { display: "inline-block" }
            }
            onClick={this.toggleFollow}
          >
            {this.state.isFollow ? `언팔로우` : `팔로우`}
          </div>
          <Link to="/userInfo">
            <div
              id="user-info"
              style={
                this.state.same
                  ? { display: "inline-block" }
                  : { display: "none" }
              }
            >
              프로필 편집
            </div>
          </Link>
          <div id="user-follow">
            <ul>
              <li>
                게시물 <b>{this.props.feedNum}</b>
              </li>

              <Link to={`/follower/${this.props.userId}`}>
                <li>
                  팔로워 <b>{this.state.followerNum}</b>
                </li>
              </Link>

              <Link to={`/follow/${this.props.userId}`}>
                <li>
                  팔로우 <b>{this.state.followingNum}</b>
                </li>
              </Link>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default UserCard;
