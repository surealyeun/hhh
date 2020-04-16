import React from 'react';
import './userCard.scss';

class UserCard extends React.Component {
    render() {
        return (
            <div id="user-card">
                <div id="avatar"></div>
                <div id="user-info">
                    <div id="user-id">catcatgood</div>
                    <div id="user-follow">
                        <ul>
                            <li>게시물 <b>4</b></li>
                            <li>팔로워 <b>21</b></li>
                            <li>팔로우 <b>29</b></li>
                        </ul>
                    </div>
                    <div id="user-desc">
                        <b>이름</b>
                        안녕하세요 !
                    </div>
                </div>
            </div>
        );
    }
}

export default UserCard;