import React from "react";
import MainSNS from "./MainSNS";
import { Link } from "react-router-dom";
import axios from "axios";
import icon from "../image/teacher.png";
import iconClose from "../image/close.png";
import userIcon from "../image/user.png";
import "./Main.scss";

// const username: string | null = sessionStorage.getItem("username");

export interface Comment {
  created: number[];
  updated: number[];
  id: number;
  text: string;
  writer_id: number;
  board_id: number;
  parents_id?: any;
  username: string;
  avatar: string;
}

export interface Feed {
  created: number[];
  updated: number[];
  id: number;
  writer_id: number;
  address_gu: string;
  content: string;
  store_id?: number;
  location_id?: number;
  loc_name: string;
  likes: number;
  username: string;
  photos: string[];
  avatar: string;
  comments: Comment[];
  pressLike: boolean;
}

class Main extends React.Component {
  state = {
    isLog: false,
    isSearch: false,
    isSns: false,
    feedlist: Array<Feed>(),
    rand: new Date(),
  };

  constructor(props: any) {
    super(props);

    this.state = {
      ...this.state,
      isLog: sessionStorage.getItem("username") ? true : false,
    };
  }

  componentWillMount() {}

  componentDidMount() {
    const username: string | null = sessionStorage.getItem("username");
    if (username) {
      axios({
        method: "get",
        url: "http://13.125.113.171:8000/feedlist/follow/" + username,
      })
        .then((res) => {
          console.log("results : ");
          console.log(res.data);
          this.setState({
            feedlist: res.data,
          });
        })
        .catch((err) => {
          console.log(err);
        });
    }
  }

  search = () => {
    this.setState({
      isSearch: !this.state.isSearch,
    });
  };

  logout = () => {
    sessionStorage.clear();
    console.log("logout");
    this.setState({
      isLog: false,
      isSns: false,
    });
  };

  closeSearch = () => {
    this.setState({
      isSearch: false,
    });
  };

  snsOpen = () => {
    if (this.state.isLog) {
      this.setState({
        isSns: !this.state.isSns,
      });
    } else {
      alert("SNS는 로그인 후에 사용 가능합니다.");
    }
  };

  render() {
    const username: string | null = sessionStorage.getItem("username");
    const avatar: string | null =
      "http://13.125.113.171:8000" + sessionStorage.getItem("avatar");
    return (
      <div className="main">
        {this.state.isSns ? (
          <div className="main-feed">
            {this.state.feedlist.map((feed, i) => {
              return (
                <>
                  <MainSNS
                    created={feed.created}
                    updated={feed.updated}
                    id={feed.id}
                    writer_id={feed.writer_id}
                    address_gu={feed.address_gu}
                    content={feed.content}
                    store_id={feed.store_id}
                    location_id={feed.location_id}
                    loc_name={feed.loc_name}
                    likes={feed.likes}
                    username={feed.username}
                    photos={feed.photos}
                    avatar={feed.avatar}
                    comments={feed.comments}
                    pressLike={feed.pressLike}
                  />
                </>
              );
            })}
          </div>
        ) : (
          <></>
        )}

        <div className={this.state.isSns ? `landing sns` : `landing`}>
          <div className="item title">
            <div className="title-head">
              <div className="log">
                {this.state.isLog ? (
                  <div>
                    <div className="user">
                      <Link to="/userInfo">
                        <img
                          className="user-profile"
                          src={
                            avatar.substr(avatar.length - 4, 4) == "null"
                              ? userIcon
                              : avatar
                          }
                          alt="user_profile"
                        />
                        <h2 className="username">{username}</h2>
                      </Link>
                    </div>
                    <div className="logout">
                      <button onClick={this.logout}>
                        {/* <h3>logout</h3> */}
                        <img
                          className="logout-btn"
                          src="https://image.flaticon.com/icons/svg/1828/1828427.svg"
                          alt="logout"
                        />
                      </button>
                    </div>
                  </div>
                ) : (
                  <div className="login">
                    <Link to="/login">
                      <img
                        className="login-btn"
                        src="https://image.flaticon.com/icons/svg/1828/1828395.svg"
                        alt="login"
                      />
                    </Link>
                  </div>
                )}
              </div>
              {this.state.isSns ? (
                <></>
              ) : (
                <>
                  <div className="search">
                    <button onClick={this.search}>
                      <p>ㅎㅎㅎ?</p>
                      <img className="search-btn" src={icon} alt="search" />
                    </button>
                  </div>
                </>
              )}
            </div>
            {this.state.isSearch ? (
              <div className="search-input">
                <div className="desc" onClick={this.closeSearch}>
                  <h2>
                    <span>ㅎㅎㅎ</span> 프로젝트의 <span>알고리즘</span>은?
                  </h2>
                  <p>🔥🔥🔥 핫플레이스 기준 🔥🔥🔥</p>
                  <p>👪 인구수 기준 (서울시 생활인구) 👪</p>
                  <br />
                  <p>1-1) 휴일과 평일의 인구수 차이: 15점 만점</p>
                  <p>1-2) 6개월 전과 현재 인구수 차이: 18점 만점</p>
                  <br />
                  <p>💵 매출 비교 (카드사 데이터) 💵</p>
                  <p>쇼핑 / 음식 / 숙박 / 교통 / 취미 / 미용 데이터</p>
                  <p>2-1) 휴일과 평일의 매출 차이: 20점 만점</p>
                  <p>2-2) 4개월 전과 현재 매출액 차이: 18점 만점</p>
                  <br />
                  <br />
                  <p>👩‍💻👩‍💻👩‍💻 맞춤 정보 기준 👨‍💻👨‍💻👨‍💻</p>
                  <br />
                  <p>사용자가 장소에 추가한 별점 기준에 따라</p>
                  <p>사용자에 맞춘 추천 장소들을 표시합니다.</p>
                  <p>데이터가 많아질 수록 ㅎㅎㅎ는</p>
                  <p>더 똑똑해져 알맞은 장소를 추천합니다!</p>
                  <img
                    className="close"
                    src={iconClose}
                    alt="close"
                    onClick={this.closeSearch}
                  />
                </div>
              </div>
            ) : (
              <></>
            )}
            <br />
            <br />
            <br />
            <h1>
              ㅎ<br />ㅎ<br />ㅎ
            </h1>
            <h4>
              <span id="h4-1">핫,</span>
              <br />
              <span id="h4-2">힙,</span>
              <br />
              <span id="h4-3">힐링,</span>
              <br />
              <span id="h4-4">플레이스</span>
            </h4>
            <div
              className={
                this.state.isSns ? `title-foot mainp` : `title-foot sns`
              }
              onClick={this.snsOpen}
            >
              {this.state.isSns ? (
                <h5 id="main">MAIN &gt;&gt;</h5>
              ) : (
                <h5 id="sns">&lt;&lt; SNS</h5>
              )}
            </div>
          </div>
          <div className="item mapFrame">
            <iframe
              className="map"
              src="../map.html"
              frameBorder="0"
              key={this.state.rand.toString()}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default Main;
