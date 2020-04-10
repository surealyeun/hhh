import React, { Component } from 'react';
import ScrollMenu from 'react-horizontal-scrolling-menu';
import './ScrollCard.css';

// list of items
const list = [
  { name: '미술관', url: 'https://bit.ly/2JJlVsz' },
  { name: '카페', url: 'https://bit.ly/2V93eDV' },
  { name: '식당', url: 'https://lh3.googleusercontent.com/proxy/YywCNOt_yt5ZWiQHQYeNJkpqTkf4QH-nO55_QR6TBKswX4I4Ftv7pZxLw8ytPf4K-6kiPKP2Z9CdLTDaflmuZ0rJxHC7Y9aPui_oP9KeHqEsJeZIczpu5vHxaXyp0kcvFjcry7ZKUIhwmsH1_ZV-fw' },
  { name: '영화관', url: 'https://lh3.googleusercontent.com/proxy/8bu7MFn66Xozn1v5PCBTmbHWJBU-AW2nS3o7AnlZIxErr5qNB8Z7Pnz04upogsvbj78yWM_1NQxdkdIcExMl9CJWQygjn-yj8KPkS3RJua1ZmiCRJ3dKUG0TJTrx9pB2H0SZ1oSg42jcIOMd319fZg' },
  { name: '공연장', url: 'https://post-phinf.pstatic.net/MjAxNzA4MTRfNjAg/MDAxNTAyNjM3MDI1ODU3.Q9F6L9jsS-ZeUjTLpPKzHJgopHPVuYJgSghQ-FkZr_kg.AtH72-p5Nlu1LQ_MBQWk_te2TMbSmJ4wlQqLe1k-s8og.JPEG/364.jpg?type=w1200' },
  { name: '극장', url: 'https://media.timeout.com/images/103479859/630/472/image.jpg' },
  { name: '1', url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQhkymP_9vhs1_RDNCkOac1UvtJFplI9x_TiSv_bo-jCwBh6k4f&usqp=CAU' },
  { name: '2', url: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQ33rYNURslMwCKWLBxu_EJexpsBxF7EuozTIUn9yeHXCHo_Ukl&usqp=CAU' },
  { name: '3', url: 'https://www.travelnbike.com/news/photo/201801/52230_67323_955.jpg' },
  { name: '4', url: 'https://lh3.googleusercontent.com/proxy/_Vj4e4NtIexA512X1B9A382gAdxy0nWQZVEQqIE87cLutTx1E37V54LEbQPMopTCkTXnjLK0nXm9SNzboDBU1o2I62Z8mPBMIHjtKtPQfEBi-JQ' },
  { name: '5', url: 'https://t1.daumcdn.net/cfile/tistory/99306D485E36EE3D27' },
  { name: '6', url: 'https://lh3.googleusercontent.com/proxy/yl1muNHAn6Tu7I19ZFiR-nhMnoshPt0Mk0SD9OznqZCFeVI8l5yv6AioFk1f_c0OdGY4r7NK5AMHlyIdsA9iJQjzLc8SkoqAC2E64m6VALRjwDfEaoBfjcCvEoHNAjh0GsI6ic8yCri49-E39VqFae4sib34OIoxI9B4ZubWx9vRBGSngNzegULBRs46UqlAP10iYAYL_pa_OsKxZRw1dHSigkvyY7Ye66S6rirx208wPw1F43gtL3UJNYo3btPNYIlpf6bX9on3cFQNLXslKBTHE9FPsE-xXTL5WujETLiMSaLIwK07Il6T__C9hK9CMIEHTTyWJyYyabZbeCKJURf9QC0rs3kDdWccftTcTrye_w' },
  { name: '7', url: 'https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile6.uf.tistory.com%2Fimage%2F9967924F5D2DC06805EE27' },
  { name: '8' },
  { name: '9' },
  { name: '10' },
  { name: '11' },
  { name: '12' },
  { name: '13' },
  { name: '14' },
  { name: '15' },
  { name: '16' },
  { name: '17' },
  { name: '18' },
  { name: '19' },
  { name: '20' },
  { name: '21' }
];

// One item component
// selected prop will be passed
const MenuItem = ({text, url, selected}) => {
  return <div
    className={`menu-item ${selected ? 'active' : ''}`}
    >{text}</div>,
    <div>
      &nbsp;&nbsp;&nbsp;
      <img className="CardImage" src={url} />
    </div>
};

// All items component
// Important! add unique key
export const Menu = (list, selected) =>
  list.map(el => {
    const { name, url } = el;

    return <MenuItem text={name} url={url} key={name} selected={selected} />;
  });


const Arrow = ({ text, className }) => {
  return (
    <div
      className={className}
    >{text}</div>
  );
};


// const ArrowLeft = Arrow({ text: '⏪', className: 'arrow-prev' });
// const ArrowRight = Arrow({ text: '⏩', className: 'arrow-next' });

const selected = 'item1';

class ScrollCard extends Component {
  constructor(props) {
    super(props);
    // call it again if items count changes
    this.menuItems = Menu(list, selected);
  }

  state = {
    selected
  };

  onSelect = key => {
    this.setState({ selected: key });
  }


  render() {
    const { selected } = this.state;
    // Create menu from items
    const menu = this.menuItems;

    return (
      <div className="App">
        <ScrollMenu
          data={menu}
          // arrowLeft={ArrowLeft}
          // arrowRight={ArrowRight}
          selected={selected}
          onSelect={this.onSelect}
        />
      </div>
    );
  }
}

export default ScrollCard;