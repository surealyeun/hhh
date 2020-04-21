import React from "react";
import { Link, Redirect, useHistory } from "react-router-dom";
import "./Header.scss";

const username: string | null = sessionStorage.getItem("username");

class Header extends React.Component {
    state = {
        isLog: false,
        isSearch: false,
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

    render() {
        return (
                <div className="Header">
                    <div className="search">
                        <button onClick={this.search}>
                            <img
                                className="search-btn"
                                src="https://image.flaticon.com/icons/svg/149/149852.svg"
                                alt="search"
                            />
                        </button>
                    </div>
                    <Link to="/">
                    <h1 className="title">
                        ㅎ<br />
                        ㅎ<br />
                        ㅎ<br />
                    </h1>
                    </Link>
                    {this.state.isLog ? (
                        <div>
                            <div className="user">
                                <Link to="">
                                    <img
                                        className="user-profile"
                                        src="https://image.flaticon.com/icons/svg/1738/1738760.svg"
                                        alt="user_profile"
                                    />
                                    {/* <h2 className="username">{username}</h2> */}
                                </Link>
                            </div>
                            <div className="logout">
                                <button onClick={this.logout}>
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
        );
    }
}

export default Header;
