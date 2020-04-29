import React from "react";
import Slide from "./Slide";
import axios from "axios";
import { Link } from "react-router-dom";
import { HeartOutlined, HeartFilled } from "@ant-design/icons";
import "./MainSNS.scss";

const username: string | null = sessionStorage.getItem("username");
const url: string = "http://13.125.113.171:8000";

export interface Comment {
    created?: number[];
    updated?: number[];
    id?: number;
    text: string;
    writer_id?: number;
    board_id?: number;
    parents_id?: any;
    username: string;
    avatar: string;
}

interface Props {
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

class MainSNS extends React.Component<Props> {
    state = {
        isLike: this.props.pressLike,
        likes: this.props.likes,
        text: "",
        comments: this.props.comments,
    };

    componentDidMount() {
        // console.log(this.props);
        // console.log(avatar);
    }

    clickLike = () => {
        if (this.state.isLike) {
            // cancle like
            console.log("delete");
            this.setState({
                likes: this.state.likes - 1,
                isLike: !this.state.isLike,
            });
            axios({
                method: "delete",
                url:
                    "http://13.125.113.171:8000/board/like/delete/" +
                    username +
                    "/" +
                    this.props.id,
            })
                .then((res) => {
                    console.log(res.data);
                })
                .catch((err) => {
                    console.log("fail delete like", err);
                });
        } else {
            // like
            console.log("like");
            this.setState({
                likes: this.state.likes + 1,
                isLike: !this.state.isLike,
            });
            axios({
                method: "post",
                url: url + "board/like/post/" + username + "/" + this.props.id,
            })
                .then((res) => {
                    console.log(res.data);
                })
                .catch((err) => {
                    console.log("fail like", err);
                });
        }
    };

    text = (comm: string) => {
        this.setState({
            text: comm,
        });
        // console.log(comm);
    };

    comment = () => {
        console.log("comment");
        const avatarr: string|null = url+sessionStorage.getItem("avatar");
        const id: string|null = sessionStorage.getItem("id");
        
        if (username != null && avatarr) {
            var newComm: Comment = {
                text: this.state.text,
                username: username,
                avatar: avatarr,
            };
            var updateComm = this.state.comments;
            updateComm.push(newComm);
            this.setState({
                comments: updateComm,
            });
        }

        axios({
            method: "post",
            url: "http://13.125.113.171:8000/comment/post/"+this.props.id+"/"+id+"/"+this.state.text,
            // headers: {'content-type': 'application/json'},
            // data: {
            //     text: this.state.text,
            //     writer: id,
            //     board: this.props.id,
            // },
        })
            .then((res) => {
                console.log("comment", res);
            })
            .catch((err) => {
                console.log("comment error", err);
            });
    };

    render() {
        const user: any | null = sessionStorage.getItem("user");
        return (
            <div className="MainSNS">
                <div className="feed-left">
                    <div className="pic">
                        <Slide photos={this.props.photos} />
                    </div>
                </div>
                <div className="feed-right">
                    <div className="user">
                        <div className="profile">
                            <img src={this.props.avatar} alt="profile" />
                        </div>
                        <div className="id">
                            <p className="text">
                                <b>{this.props.username}</b>
                            </p>
                        </div>
                    </div>
                    <div className="content">
                        {/* 작성자, 리플들 */}
                        <div className="post">
                            <div className="profile">
                                <img src={this.props.avatar} alt="profile" />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>{this.props.username}</b> {this.props.content}
                                </p>
                            </div>
                            <div className="spot">
                                <Link
                                    to={
                                        this.props.location_id
                                            ? `/place/` + this.props.location_id
                                            : `/store/` + this.props.store_id
                                    }
                                >
                                    <img
                                        className="location"
                                        src="https://image.flaticon.com/icons/svg/447/447031.svg"
                                        alt="location"
                                    />
                                    <p>{this.props.loc_name}</p>
                                </Link>
                            </div>
                        </div>
                        {this.state.comments.map((comment, i) => {
                            return (
                                <>
                                    <div className="comment">
                                        <div className="profile">
                                            <img
                                                src={
                                                    comment.avatar
                                                        ? comment.avatar
                                                        : "https://image.flaticon.com/icons/svg/1738/1738760.svg"
                                                }
                                                alt="profile"
                                            />
                                        </div>
                                        <div className="te">
                                            <p className="text">
                                                <b>{comment.username}</b> {comment.text}
                                            </p>
                                        </div>
                                    </div>
                                </>
                            );
                        })}
                    </div>
                    <div className="like">
                        <div className="like-heart">
                            <p className="like" onClick={this.clickLike}>
                                {this.state.isLike ? <HeartFilled /> : <HeartOutlined />}
                                <span className="num">좋아요 {this.state.likes}개</span>
                            </p>
                        </div>
                    </div>
                    <div className="mk-comment">
                        <textarea
                            placeholder="댓글 달기"
                            onChange={(e) => this.text(e.target.value)}
                        />
                        <button className="comment-btn" onClick={this.comment}>
                            게시
                        </button>
                    </div>
                </div>
            </div>
        );
    }
}

export default MainSNS;
