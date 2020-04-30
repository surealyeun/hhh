import React from "react";
import { Link } from "react-router-dom";
import Feed from "./feed/Feed";
import UserCard from "./userCard/userCard";
import Follow from "./follow/Follow";
import "./FeedList.scss";

class FeedList extends React.Component {
  render() {
    return (
      <div id="feed-list">
        <Follow />
        <UserCard />

        <input type="text" id="search-bar" placeholder="검색"></input>
        <div id="list">
          <div className="row">
            <Link to="/feedDetail">
              <Feed url="https://image.shutterstock.com/image-photo/honolulu-hawaii-dec-23-2018-260nw-1271997817.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://t1.daumcdn.net/liveboard/ttimes/efb7ffc328f545b7816049f00b450724.JPG"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://media-cdn.tripadvisor.com/media/photo-s/0a/02/f1/ff/slice-of-waikiki-pizza.jpg"></Feed>
            </Link>
          </div>

          <div className="row">
            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2014/07/Lau-Lau.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2015/02/IMG_5957.jpg"></Feed>
            </Link>

            <Link to="/feedDetail">
              <Feed url="https://www.myhawaii.kr/wp-content/uploads/2018/08/IMG_4630.jpg"></Feed>
            </Link>
          </div>
        </div>
      </div>
    );
  }
}

export default FeedList;
