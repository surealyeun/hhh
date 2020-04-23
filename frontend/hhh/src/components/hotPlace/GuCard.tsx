import React from 'react';
import './GuCard.scss';

class UserCard extends React.Component {
    render() {
        return (
            <div id="Gu-card">
                <div id="avatar">
                    <img src="https://pbs.twimg.com/profile_images/491461147439009792/BU9yRHVK_400x400.png" alt="" />
                </div>
                <div id="user-info">
                    <div id="user-id">JONGNO</div>
                    <div id="user-follow">
                        <ul>
                            <li>게시물 <b>4</b></li>
                            <li>팔로워 <b>21</b></li>
                            <li>팔로우 <b>29</b></li>
                        </ul>
                    </div>
                    <div id="user-desc">
                        <b>종로</b>
                        사람중심 명품도시 종로
                    </div>
                </div>
            </div>
        );
    }
}

export default UserCard;