import React from "react";
import { Link } from "react-router-dom";
import Feed from "./feed/Feed";
import UserCard from "./userCard/userCard";
import "./FeedList.scss";
import axios from "axios";

class FeedList extends React.Component {
  state = {
    userId: 0,
    userName: sessionStorage.getItem("username"),
    userAvatar: "",
    feedList: [],
    feedNum: 0,
  };

  async componentDidMount() {
    await axios
      .get("http://13.125.113.171:8000/feedlist/user/" + this.state.userName)
      .then((res) => {
        this.setState({
          ...this.state,
          userId: res.data[0].id,
          userAvatar: res.data[0].avatar,
          feedList: res.data,
          feedNum: res.data.length,
        });

        console.log(this.state);
      });
  }

  render() {
    return (
      <div id="feed-list">
        <UserCard
          avatarPic={this.state.userAvatar}
          userId={this.state.userId}
          feedNum={this.state.feedNum}
        />

        <input type="text" id="search-bar" placeholder="검색"></input>
        <div id="list">
          <div className="row">
            {this.state.feedList.map((data: any) => (
              <Feed url={data.photos[0]}></Feed>
            ))}

            {/* <Link to="/feedDetail">
              <Feed url="https://image.shutterstock.com/image-photo/honolulu-hawaii-dec-23-2018-260nw-1271997817.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://t1.daumcdn.net/liveboard/ttimes/efb7ffc328f545b7816049f00b450724.JPG"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://media-cdn.tripadvisor.com/media/photo-s/0a/02/f1/ff/slice-of-waikiki-pizza.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2014/07/Lau-Lau.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2015/02/IMG_5957.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2018/08/IMG_4630.jpg"></Feed>
            </Link> */}
          </div>
        </div>
      </div>
    );
  }
}

export default FeedList;
