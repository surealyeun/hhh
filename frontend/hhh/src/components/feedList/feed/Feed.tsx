import React from "react";
import "./Feed.scss";

class Feed extends React.Component<
  { url: string },
  { bgColor: string; display: string }
> {
  constructor(props: { url: string }) {
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
    this.setState({ bgColor: "rgba(0, 0, 0, 0.3)", display: "block" });
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
                좋아요 <b>12</b>
              </li>
              <li>
                댓글 <b>3</b>
              </li>
            </ul>
          </div>
        </div>
      </div>
    );
  }
}

export default Feed;
