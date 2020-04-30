import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import "./Follow.scss";

class Follower extends Component {
  state = {
    userId: window.location.href.split("/")[4],
    loginUserName: sessionStorage.getItem("username"),
    followList: [],
    originUserName: sessionStorage.getItem("originUserName"),
  };

  async componentDidMount() {
    await axios
      .get("http://13.125.113.171:8000/follower/" + Number(this.state.userId))
      .then((res) => {
        console.log(res.data);

        this.setState({
          followList: res.data,
        });
      });
  }

  render() {
    return (
      <div id="follow" style={{ display: "block" }}>
        <div id="follow-list">
          <div id="follow-text">
            팔로워
            <Link to={`/feedList/${this.state.originUserName}`}>
              <div id="close-btn">X</div>
            </Link>
          </div>
          <ul>
            {this.state.followList.map((data: any) => (
              <li>
                <Link to={`/feedList/${data.username}`}>
                  <img
                    src={`http://13.125.113.171:8000` + data.avatar}
                    alt=""
                  ></img>
                </Link>
                <Link to={`/feedList/${data.username}`}>
                  <div className="id">{data.username}</div>
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
}

export default Follower;
