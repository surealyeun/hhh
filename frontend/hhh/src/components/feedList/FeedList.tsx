import React from 'react';
import Feed from './Feed';

class FeedList extends React.Component {
    render() {
        return (
            <div id="comp-feed-list">
                <div id="searchBar"></div>
                <div id="list">
                    <Feed></Feed>
                </div>
            </div>
        );
    }
}

export default FeedList;