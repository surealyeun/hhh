import React from 'react';
import './GuCard.scss';

class UserCard extends React.Component {
    render() {
        return (
            <div id="Gu-card">
                <div id="avatar">
                    <img src="https://lh3.googleusercontent.com/proxy/x6TZXn41daV-3IyfzQClDK1MOW48goNOIsyC5a_A4ErnZF6rsvt5twPrQrfuNBCiez07LfspemxfEhM3MW0NWC18oR3oNM-N2WLVl46uwhlJsN5aYwsUu3NKx46jjoti0aRJMbjhKiJRUS7KVUqvP2I9orLP3ftFk_a-aZqXnwaeaid1JbuJoHSraqtzYsaRq_blG8LI" alt="" />
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