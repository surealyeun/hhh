import React from "react";
import SlideImg from "./SlideImg";
import Slide from "./Slide";
import { HeartOutlined, HeartFilled } from "@ant-design/icons";
import "./MainSNS.scss";

class MainSNS extends React.Component {
    state = {
        isLike: false,
    };

    clickLike = () => {
        this.setState({
            isLike: !this.state.isLike,
        });
    };

    render() {
        return (
            <div className="MainSNS">
                <div className="feed feed-left">
                    <div className="pic">
                        <Slide />
                    </div>
                </div>
                <div className="feed feed-right">
                    <div className="user">
                        <div className="profile">
                            <img
                                src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/93818837_131608151785158_3965098545993740587_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=wvnkNF-vXrYAX8A33uX&oh=8f358207c784034a74e842729e4ecf25&oe=5ECA5FDA"
                                alt="profile"
                            />
                        </div>
                        <div className="id">
                            <p className="text">
                                <b>idididid</b>
                            </p>
                        </div>
                    </div>
                    <div className="content">
                        {/* 작성자, 리플들 */}
                        <div className="post">
                            <div className="profile">
                                <img
                                    src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/93818837_131608151785158_3965098545993740587_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=106&_nc_ohc=wvnkNF-vXrYAX8A33uX&oh=8f358207c784034a74e842729e4ecf25&oe=5ECA5FDA"
                                    alt="profile"
                                />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>idididid</b> blahblahblahblahblahblahblahblahblah 줄바꿈은
                                    언제 생기는 걸까 abcdefghijklmnopqrstuvwxyz 이 사진에 대해서
                                    설명할거야 두 사람이 있어 각자 책을 열심히 보고있지 한 명은 소파
                                    위에 한 명은 바닥에 앉아있어
                                </p>
                            </div>
                        </div>
                        <div className="comment">
                            <div className="profile">
                                <img
                                    src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/94100839_2941295502580071_3479324562767351595_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KNSjtdSu2UsAX8zkoXj&oh=1b4b850df518043e65cc2acabc4fa55f&oe=5ECC4C3B"
                                    alt="profile"
                                />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>didididi</b> 나는 댓글을 달거야 아주 좋아
                                </p>
                            </div>
                        </div>
                        <div className="comment">
                            <div className="profile">
                                <img
                                    src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/94100839_2941295502580071_3479324562767351595_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KNSjtdSu2UsAX8zkoXj&oh=1b4b850df518043e65cc2acabc4fa55f&oe=5ECC4C3B"
                                    alt="profile"
                                />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>didididi</b> 나는 댓글을 달거야 아주 좋아
                                </p>
                            </div>
                        </div>
                        <div className="comment">
                            <div className="profile">
                                <img
                                    src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/94100839_2941295502580071_3479324562767351595_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KNSjtdSu2UsAX8zkoXj&oh=1b4b850df518043e65cc2acabc4fa55f&oe=5ECC4C3B"
                                    alt="profile"
                                />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>didididi</b> 나는 댓글을 달거야 아주 좋아
                                </p>
                            </div>
                        </div>
                        <div className="comment">
                            <div className="profile">
                                <img
                                    src="https://scontent-ssn1-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/94100839_2941295502580071_3479324562767351595_n.jpg?_nc_ht=scontent-ssn1-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KNSjtdSu2UsAX8zkoXj&oh=1b4b850df518043e65cc2acabc4fa55f&oe=5ECC4C3B"
                                    alt="profile"
                                />
                            </div>
                            <div className="te">
                                <p className="text">
                                    <b>didididi</b> 나는 댓글을 달거야 아주 좋아
                                </p>
                            </div>
                        </div>
                    </div>
                    <div className="like">
                        <div className="like-heart" onClick={this.clickLike}>
                        <p className="like">
                            {this.state.isLike ? <HeartFilled /> : <HeartOutlined />}
                            <span className="num">좋아요 202개</span></p>
                        </div>
                    </div>
                    <div className="mk-comment">
                        <textarea placeholder="댓글 달기" />
                        <button className="comment-btn">게시</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default MainSNS;
