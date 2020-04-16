import React from 'react';
import './Feed.scss';

class Feed extends React.Component<{ url: string }, { flipped: boolean }> {
    constructor(props: { url: string }) {
        super(props);
        this.state = {
            flipped: false
        };
    }

    mouseOut() {
        this.setState({ flipped: false });
    }

    mouseOver() {
        this.setState({ flipped: true });
    }

    render() {
        return (
            <div className="feed" onMouseOut={() => this.mouseOut()} onMouseOver={() => this.mouseOver()}>
                <img src={this.props.url} alt="" />
            </div>
        );
    }
}

export default Feed;
