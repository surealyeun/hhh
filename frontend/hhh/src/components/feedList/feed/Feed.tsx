import React from 'react';
import './Feed.scss';

class Feed extends React.Component<{}, { flipped: boolean }> {
    constructor(props: {}) {
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
                {this.state.flipped}
            </div>
        );
    }
}

export default Feed;
