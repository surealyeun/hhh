import React from "react";
import MainSNS from "./MainSNS";
import { Link } from "react-router-dom";
import axios from "axios";
import "./Main.scss";

const username: string | null = sessionStorage.getItem("username");

class Main extends React.Component {
    state = {
        isLog: false,
        isSearch: false,
        isSns: false,
    };

    constructor(props: any) {
        super(props);

        this.state = {
            ...this.state,
            isLog: sessionStorage.getItem("username") ? true : false,
        };
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
        });
    };

    closeSearch = () => {
        this.setState({
            isSearch: false,
        });
    };

    snsOpen = () => {
        axios({
            method: "get",
            url: "http://13.125.113.171:8000/feedlist/opwer032",
        }).then(res => {
            console.log(res.data);
        }).catch(err => {
            console.log(err);
        })
        this.setState({
            isSns: !this.state.isSns,
        });
    };

    render() {
        return (
            <div className="main">
                
                {this.state.isSns ? 
                    <div className="main-feed"><MainSNS /></div>: <></>}
                
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
                                    <img
                                        className="search-btn"
                                        src="https://image.flaticon.com/icons/svg/149/149852.svg"
                                        alt="search"
                                    />
                                </button>
                            </div>
                            {this.state.isSearch ? (
                                <div className="search-input">
                                    <input type="text"></input>
                                    <img
                                        className="close"
                                        src="https://image.flaticon.com/icons/svg/1828/1828778.svg"
                                        alt="close"
                                        onClick={this.closeSearch}
                                    />
                                </div>
                            ) : (
                                <></>
                            )}
                        </div>
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
                        <div className={this.state.isSns ? `title-foot mainp` : `title-foot sns`} onClick={this.snsOpen}>
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
