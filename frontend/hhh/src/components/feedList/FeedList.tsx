import React from 'react';
import Feed from './feed/Feed';
import UserCard from './userCard/userCard';
import './FeedList.scss';

class FeedList extends React.Component {
    render() {
        return (
            <div id="feed-list">
                <UserCard />

                <input type="text" id="search-bar" placeholder="검색"></input>
                <div id="list">
                    <div className="row">
                        <Feed url="https://lh3.googleusercontent.com/proxy/9UZA-I76mE5cL7z0HIN5OBVDQIJPbtnt6XMSoXb9nNUNvwyoTjYqiPLicQAndqKQiRlVEhWEhMfFQ9y8zvA91IULEmU1qLI"></Feed>
                        <Feed url="https://t1.daumcdn.net/liveboard/ttimes/efb7ffc328f545b7816049f00b450724.JPG"></Feed>
                        <Feed url="https://media-cdn.tripadvisor.com/media/photo-s/0a/02/f1/ff/slice-of-waikiki-pizza.jpg"></Feed>
                    </div>

                    <div className="row">
                        <Feed url="https://www.myhawaii.kr/wp-content/uploads/2014/07/Lau-Lau.jpg"></Feed>
                        <Feed url="https://www.myhawaii.kr/wp-content/uploads/2015/02/IMG_5957.jpg"></Feed>
                        <Feed url="https://www.myhawaii.kr/wp-content/uploads/2018/08/IMG_4630.jpg"></Feed>
                    </div>
                </div>
            </div>
        );
    }
}

export default FeedList;