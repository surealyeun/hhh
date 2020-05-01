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
  };

  async componentDidUpdate(prevProps: any) {
    if (this.props.userId !== prevProps.userId) {
      if (sessionStorage.getItem("username") === this.state.username) {
        this.setState({
          same: true,
        });
      }

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

  render() {
    return (
      <div id="user-card">
        <div id="avatar">
          <img src={this.props.avatarPic} alt="" />
        </div>
        <div id="user-info">
          <div id="user-id">{this.state.username}</div>
          <Link to="/userinfo">
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

              <Link to="/follow">
                <li>
                  팔로워 <b>{this.state.followerNum}</b>
                </li>
              </Link>

              <Link to="/follow">
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
