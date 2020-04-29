import React from "react";
import MainSNS from "./MainSNS";
import { Link } from "react-router-dom";
import axios from "axios";
import icon from "../image/teacher.png";
import iconClose from "../image/close.png";
import "./Main.scss";

const username: string | null = sessionStorage.getItem("username");

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
    };

    constructor(props: any) {
        super(props);

        this.state = {
            ...this.state,
            isLog: sessionStorage.getItem("username") ? true : false,
        };
    }

    componentDidMount() {
        if (this.state.isLog) {
            axios({
                method: "get",
                url: "http://13.125.113.171:8000/feedlist/follow/" + username,
            })
                .then((res) => {
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
        sessionStorage.removeItem("username");
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
                                            <Link to="">
                                                <img
                                                    className="user-profile"
                                                    src="https://image.flaticon.com/icons/svg/1738/1738760.svg"
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
                            <div className="search">
                                <button onClick={this.search}>
                                    <p>ㅎㅎㅎ?</p>
                                    <img className="search-btn" src={icon} alt="search" />
                                </button>
                            </div>
                        </div>
                        {this.state.isSearch ? (
                            <div className="search-input">
                                <div className="desc" onClick={this.closeSearch}>
                                    <h2>
                                        <span>ㅎㅎㅎ</span> 프로젝트의 <span>알고리즘</span>은?
                                    </h2>
                                    <p>
                                        피고 눈에 고동을 것이다. 위하여서, 그들을 우리 천고에 용기가
                                        싸인 위하여서. 이 주는 것은 대중을 발휘하기 그들의 인생을
                                        보라. 얼음과 그림자는 같이, 타오르고 속잎나고, 대중을
                                        그리하였는가? 영원히 하였으며, 생명을 인간은 것이다. 인생의
                                        되는 끝에 몸이 우리 행복스럽고 두손을 것이다. 내려온 열락의
                                        청춘의 찾아다녀도, 청춘의 청춘에서만 새 무엇이 칼이다.
                                        이상의 동산에는 너의 동력은 열락의 눈에 보이는 따뜻한
                                        끓는다. 위하여 피가 찾아다녀도, 맺어, 사막이다. 바로 그들은
                                        날카로우나 가슴에 피에 이상은 뿐이다. 이상은 별과 가장 몸이
                                        힘있다. 같으며, 불어 주며, 때까지 원질이 청춘을 그들의
                                        듣는다. 미묘한 이것은 청춘의 있다. 인생의 밥을 간에 운다.
                                        영원히 인간에 같지 긴지라 굳세게 곳이 천자만홍이 말이다.
                                        가는 청춘의 사랑의 피다. 속잎나고, 꾸며 그들은 위하여서.
                                        얼음 그것을 바로 살았으며, 크고 구하기 사는가 힘차게
                                        약동하다. 따뜻한 길을 얼마나 그것은 봄날의 아니다. 생의 곳이
                                        피어나기 같은 옷을 갑 이상 실현에 이상, 이것이다. 앞이 너의
                                        청춘을 있을 없으면 밝은 뜨고, 얼음 사막이다. 보배를 사람은
                                        그것을 사라지지 인간의 열락의 있다. 아니한 힘차게 청춘을
                                        투명하되 있으며, 없으면 간에 창공에 소금이라 약동하다. 돋고,
                                        피에 창공에 맺어, 운다. 끓는 인간이 주는 생생하며, 그들은
                                        현저하게 힘있다. 되려니와, 긴지라 같이, 얼음과 기관과 찬미를
                                        위하여, 오아이스도 있는가? 미인을 불어 가진 고동을 싸인
                                        사막이다. 천자만홍이 할지라도 황금시대를 말이다. 얼음에
                                        찬미를 인류의 쓸쓸하랴? 그러므로 그들은 품었기 사라지지 곳이
                                        주는 속잎나고, 이는 봄바람이다. 꽃이 그들은 무엇을 인간에
                                        같이, 풀밭에 사막이다.
                                    </p>
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
                            className={this.state.isSns ? `title-foot mainp` : `title-foot sns`}
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
                        <iframe className="map" src="../map.html" frameBorder="0" />
                    </div>
                </div>
            </div>
        );
    }
}

export default Main;
