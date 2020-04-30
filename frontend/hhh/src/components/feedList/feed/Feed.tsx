import React from "react";
import "./Feed.scss";

class Feed extends React.Component<
  { url: string; likeNum: number; commentNum: number },
  { bgColor: string; display: string }
> {
  constructor(props: { url: string; likeNum: number; commentNum: number }) {
    super(props);
    this.state = {
      bgColor: "rgba(0,0,0,0)",
      display: "none",
    };
  }

  mouseOut() {
    this.setState({ bgColor: "rgba(0, 0, 0, 0)", display: "none" });
  }

  mouseOver() {
    this.setState({ bgColor: "rgba(0, 0, 0, 0.4)", display: "block" });
  }

  render() {
    return (
      <div
        className="feed"
        onMouseOut={() => this.mouseOut()}
        onMouseOver={() => this.mouseOver()}
      >
        <img src={this.props.url} alt="" />
        <div
          className="feedCover"
          style={{
            backgroundColor: this.state.bgColor,
            display: this.state.display,
          }}
        >
          <div className="feedCoverText">
            <ul>
              <li>
                좋아요 <b>{this.props.likeNum}</b>
              </li>
              <li>
                댓글 <b>{this.props.commentNum}</b>
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default Feed;
