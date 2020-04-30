import React, { Component } from "react";
import "./FeedDetail.scss";

class FeedDetail extends Component {
  render() {
    return (
      <div id="feed-detail">
        <div id="user-id">
          <img
            className="user-pic"
            src="https://ssolmarket.com/wp-content/uploads/2019/08/%EC%83%B43.jpg"
            alt=""
          />
          <div id="id">catcatgood</div>
        </div>

        <div id="feed-img">
          <img
            src="https://imagescdn.gettyimagesbank.com/500/16/809/862/0/522478244.jpg"
            alt=""
          ></img>
        </div>

        <div id="feed-inside">
          <div id="feed-btns"></div>
          <div id="likes">좋아요 30개</div>
          <div id="feed-text">
            <ul>
              <li>
                <div className="id">testUser1</div>
                <div className="text">Hello !</div>
              </li>

              <li>
                <div className="id">testUser2</div>
                <div className="text">Looks pretty</div>
              </li>
            </ul>
          </div>

          <div id="make-text">
            <input type="text" placeholder="댓글 달기..." />
            <div id="make">게시</div>
          </div>
        </div>
      </div>
    );
  }
}

export default FeedDetail;
