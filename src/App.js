import React, { Component } from 'react';
//import logo from './logo.svg';
import styles from './App.css';
import Select from 'react-select' //add for select box
import { RenderAfterNavermapsLoaded, NaverMap, Marker, Circle } from 'react-naver-maps'; // 패키지 불러오기
import ReactPlayer from 'react-player'; //for video render
import { Helmet } from 'react-helmet'; //for 배경색
import Typical from 'react-typical'; //for type effect
import firebase from 'firebase';
import { text } from 'body-parser';

//import TestJSON from 

const databaseURL = "https://tracking-50971.firebaseio.com/word.json";

let todoId = 0 // todo 아이템의 id를 증가시키며 저장하는 변수

const video_options = [{ value: 'videos/1_bf1.mp4', label: "CAM1" }
  , { value: 'videos/1_bf2.mp4', label: "CAM2" }
  , { value: 'videos/1_bf3.mp4', label: "CAM3" }]

//value 4 = cam1
const frame_options = [
  { value1: 'videos/1_ys1.mov', value2: "******* find 1_ys1 *******\n2_ys1.json\nCAM2_8:30", value3: '0.5', value4: '0.5', value5: '0', value1_1: 'videos/2_ys1.mov', value1_2: null, value1_3: null, value1_4: null, text1: 'CAM2_8:30', text2: null, text3: null, text4: null, label: "8:00" },
  { value1: 'videos/2_ys1.mov', value2: '******* find 2_ys1 *******\n1_ys1.json\nCAM1_8:00', value3: '0.5', value4: '0.5', value5: '0', value1_1: 'videos/1_ys1.mov', value1_2: null, value1_3: null, value1_4: null, text1: 'CAM1_8:00', text2: null, text3: null, text4: null, label: "8:30" },
  { value1: 'videos/3_hj2.mov', value2: "******* find 3_hj2 *******\n1_hj1.json\nCAM1_10:30\n2_hj2.json\nCAM2_13:00\n2_hj1.json\nCAM2_13:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/1_hj1.mov', value1_2: 'videos/2_hj2.mov', value1_3: 'videos/2_hj1.mov', value1_4: null, text1: 'CAM1_10:30', text2: 'CAM2_13:00', text3: 'CAM2_13:30', text4: null, label: "9:00" },
  { value1: 'videos/3_bf2.mov', value2: "******* find 3_sbf2 *******\n1_sbf1.json\nCAM1_11:30\n2_sbf2.json\nCAM2_15:30\n1_sbf2.json\nCAM1_16:30\n3_sbf3.json\nCAM3_17:00\n3_sbf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/1_bf1.mov', value1_2: 'videos/2_bf2.mov', value1_3: 'videos/1_bf2.mov', value1_4: 'videos/3_bf3.mov', value1_5: 'videos/3_bf4.mov', text1: 'CAM1_11:30', text2: 'CAM2_15:30', text3: 'CAM1_16:30', text4: 'CAM3_17:00', text5: 'CAM3_17:30', label: "9:30" },
  { value1: 'videos/1_my1.mov', value2: "******* find 1_my1 *******\n3_my1.json\nCAM3_12:30", value3: '0', value4: '0.5', value5: '0.5', value1_1: 'videos/3_my1.mov', value1_2: null, value1_3: null, value1_4: null, text1: 'CAM3_12:30', text2: null, text3: null, text4: null, label: "10:00" },
  { value1: 'videos/1_hj1.mov', value2: "******* find 1_hj1 *******\n3_hj2.json\nCAM3_9:00\n2_hj2.json\nCAM2_13:00\n2_hj1.json\nCAM2_13:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_hj2.mov', value1_2: 'videos/2_hj2.mov', value1_3: 'videos/2_hj1.mov', value1_4: null, text1: 'CAM3_9:00', text2: 'CAM2_13:00', text3: 'CAM2_13:30', text4: null, label: "10:30" },
  { value1: 'videos/3_js1.mov', value2: "******* find 3_sjs1 *******\n1_sjs1.json\nCAM1_12:00\n2_sjs1.json\nCAM2_16:00", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/1_js1.mov', value1_2: 'videos/2_js1.mov', value1_3: null, value1_4: null, text1: 'CAM1_12:00', text2: 'CAM2_16:00', text3: null, text4: null, label: "11:00" },
  { value1: 'videos/1_bf1.mov', value2: "******* find 1_sbf1 *******\n3_sbf2.json\nCAM3_9:30\n2_sbf2.json\nCAM2_15:30\n1_sbf2.json\nCAM1_16:30\n3_sbf3.json\nCAM3_17:00\n3_sbf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_bf2.mov', value1_2: 'videos/2_bf2.mov', value1_3: 'videos/1_bf2.mov', value1_4: 'videos/3_bf3.mov', value1_5: 'videos/3_bf4.mov', text1: 'CAM3_9:30', text2: 'CAM2_15:30', text3: 'CAM1_16:30', text4: 'CAM3_17:00', text5: 'CAM3_17:30', label: "11:30" },
  { value1: 'videos/1_js1.mov', value2: "******* find 1_sjs1 *******\n3_sjs1.json\nCAM3_11:00\n2_sjs1.json\nCAM2_16:00", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_js1.mov', value1_2: 'videos/2_js1.mov', value1_3: null, value1_4: null, text1: 'CAM3_11:00', text2: 'CAM2_16:00', text3: null, text4: null, label: "12:00" },
  { value1: 'videos/3_my1.mov', value2: "******* find 3_my1 *******\n1_my1.json\nCAM1_10:00", value3: '0', value4: '0.5', value5: '0.5', value1_1: 'videos/1_my1.mov', value1_2: null, value1_3: null, value1_4: null, text1: 'CAM1_10:00', text2: null, text3: null, text4: null, label: "12:30" },
  { value1: 'videos/2_hj2.mov', value2: "******* find 2_hj2 *******\n3_hj2.json\nCAM3_9:00\n1_hj1.json\nCAM1_10:30\n2_hj1.json\nCAM2_13:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_hj2.mov', value1_2: 'videos/1_hj1.mov', value1_3: 'videos/2_hj1.mov', value1_4: null, text1: 'CAM3_9:00', text2: 'CAM1_10:30', text3: 'CAM2_13:30', text4: null, label: "13:00" },
  { value1: 'videos/2_hj1.mov', value2: "******* find 2_hj1 *******\n3_hj2.json\nCAM3_9:00\n1_hj1.json\nCAM1_10:30\n2_hj2.json\nCAM2_13:00", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_hj2.mov', value1_2: 'videos/1_hj1.mov', value1_3: 'videos/2_hj2.mov', value1_4: null, text1: 'CAM3_9:00', text2: 'CAM1_10:30', text3: 'CAM2_13:00', text4: null, label: "13:30" },
  { value1: 'videos/2_bf2.mov', value2: "******* find 2_sbf2 *******\n3_sbf2.json\nCAM3_9:30\n1_sbf1.json\nCAM1_11:30\n1_sbf2.json\nCAM1_16:30\n3_sbf3.json\nCAM3_17:00\n3_sbf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_bf2.mov', value1_2: 'videos/1_bf1.mov', value1_3: 'videos/1_bf2.mov', value1_4: 'videos/3_bf3.mov', value1_5: 'videos/3_bf4.mov', text1: 'CAM3_9:30', text2: 'CAM1_11:30', text3: 'CAM1_16:30', text4: 'CAM3_17:00', text5: 'CAM3_17:30', label: "15:30" },
  { value1: 'videos/2_js1.mov', value2: "******* find 2_sjs1 *******\n1_sjs1.json\nCAM1_12:00\n3_sjs1.json\nCAM3_11:00", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/1_js1.mov', value1_2: 'videos/3_js1.mov', value1_3: null, value1_4: null, text1: 'CAM1_12:00', text2: 'CAM3_11:00', text3: null, text4: null, label: "16:00" },
  { value1: 'videos/1_bf2.mov', value2: "******* find 1_sbf2 *******\n3_sbf2.json\nCAM3_9:30\n1_sbf1.json\nCAM1_11:30\n2_sbf2.json\nCAM2_15:30\n3_sbf3.json\nCAM3_17:00\n3_sbf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_bf2.mov', value1_2: 'videos/1_bf1.mov', value1_3: 'videos/2_bf2.mov', value1_4: 'videos/3_bf3.mov', value1_5: 'videos/3_bf4.mov', text1: 'CAM3_9:30', text2: 'CAM1_11:30', text3: 'CAM2_15:30', text4: 'CAM3_17:00', text5: 'CAM3_17:30', label: "16:30" },
  { value1: 'videos/3_bf3.mov', value2: "******* find 3_sbf3 *******\n3_sbf2.json\nCAM3_9:30\n1_sbf1.json\nCAM1_11:30\n2_sbf2.json\nCAM2_15:30\n1_sbf2.json\nCAM1_16:30\n3_sbf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_bf2.mov', value1_2: 'videos/1_bf1.mov', value1_3: 'videos/2_bf2.mov', value1_4: 'videos/1_bf2.mov', value1_5: 'videos/3_bf4.mov', text1: 'CAM3_9:30', text2: 'CAM1_11:30', text3: 'CAM2_15:30', text4: 'CAM1_16:30', text5: 'CAM3_17:30', label: "17:00" },
  { value1: 'videos/3_bf4.mov', value2: "******* find 3_sbf4 *******\n3_sbf2.json\nCAM3_9:30\n1_sbf1.json\nCAM1_11:30\n2_sbf2.json\nCAM2_15:30\n1_sbf2.json\nCAM1_16:30\n3_sbf3.json\nCAM3_17:00", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/3_bf2.mov', value1_2: 'videos/1_bf1.mov', value1_3: 'videos/2_bf2.mov', value1_4: 'videos/1_bf2.mov', value1_5: 'videos/3_bf3.mov', text1: 'CAM3_9:30', text2: 'CAM1_11:30', text3: 'CAM2_15:30', text4: 'CAM1_16:30', text5: 'CAM3_17:00', label: "17:30" }
]
/*value1: 'videos/1_bf2.mov', value2: "******* find 1_bf2 *******\n2_bf1.json\nCAM2_9:30\n2_bf2.json\nCAM1_15:30\n1_bf1.json\nCAM1_16:30\n3_bf4.json\nCAM3_17:30", value3: '0.5', value4: '0.5', value5: '0.5', value1_1: 'videos/2_bf1.mov', value1_2: 'videos/2_bf2.mov', value1_3: 'videos/1_bf1.mov', value1_4: 'videos/3_bf4.mov', text1: 'CAM2_9:30', text2: 'CAM1_15:30', text3: 'CAM1_16:30', text4: 'CAM3_17:30',*/
//const navermaps = window.naver.maps;

let markcolor = 0

class App extends Component {

  constructor(props) { //Datas!
    super(props)
    this.state = { //add for nodejs data
      username: null,
      videoUrl: null,
      videoUrl1: null,
      videoUrl2: null,
      videoUrl3: null,
      videoUrl4: null,
      videoUrl5: null,
      videoUrl6: null,
      text1: null,
      text2: null,
      text3: null,
      text4: null,
      text5: null,
      text6: null,
      selectedOption: null,
      markcolor1: 0,
      markcolor2: 0,
      markcolor3: 0,
      output: null,
      data: [], //firebase data 저장 공간
      word: {}
    };
    //for player
    this.player = React.createRef();
  }

  load = videoUrl => {
    this.setState({
      videoUrl
    })
  }

  load = markcolor => {
    this.setState({
      markcolor
    })
  }

  load = output => {
    this.setState({
      output
    })
  }

  handleVideoChange = videoUrl => {
    this.setState({ videoUrl: this.state.videoUrl });
    console.log(`Option selected:`, videoUrl);
  };

  handleChange = selectedOption => { //for change output
    setTimeout(() => {
      this.setState({ selectedOption })
    }, 20);
    setTimeout(() => {
      this.setState({
        videoUrl: selectedOption.value1
      })
    }, 1000);
    setTimeout(() => {
      this.setState({
        output: selectedOption.value2
      })
    }, 3000);
    setTimeout(() => {
      this.setState({
        markcolor1: selectedOption.value3
      })
    }, 3000);
    setTimeout(() => {
      this.setState({
        markcolor2: selectedOption.value4
      })
    }, 3000);
    setTimeout(() => {
      this.setState({
        markcolor3: selectedOption.value5,
        text1: selectedOption.text1,
        text2: selectedOption.text2,
        text3: selectedOption.text3,
        text4: selectedOption.text4,
        text5: selectedOption.text5,
        text6: selectedOption.text6
      })
    }, 3000);

    setTimeout(() => {
      this.setState({
        videoUrl1: selectedOption.value1_1,
        videoUrl2: selectedOption.value1_2,
        videoUrl3: selectedOption.value1_3,
        videoUrl4: selectedOption.value1_4,
        videoUrl5: selectedOption.value1_5,
        videoUrl6: selectedOption.value1_6,
      })
    }, 4000);
  };

  // componentDidMount() {
  //   setTimeout(function() { //Start the timer
  //       this.setState({render: true}) //After 1 second, set render to true
  //   }.bind(this), 1000)
  // }
  

  componentDidMount() { //for get datas (지금은 DY and HJ) from server.js
    fetch('/api/py') //http:// ... :3001을 제외. /api 직전까지는 server.js 와 http url 이 같기 때문.
      .then(res => res.json())
      .then(data => this.setState({ username: data.username }));

    // firebase.initializeApp({
    //   apiKey: "sec",
    //   authDomain: "sec",
    //   databaseURL: "sec",
    //   projectId: "sec",
    //   storageBucket: "sec",
    //   messagingSenderId: "sec",
    //   appId: "sec",
    //   measurementId: "sec"
    // });

    fetch(`${databaseURL}/word.json`) //http:// ... :3001을 제외. /api 직전까지는 server.js 와 http url 이 같기 때문.
      .then(res => { return res.json() })
      .then(word => this.setState({ word: word }));
  }

  render() {
    const {
      RenderAfterNavermapsLoaded,
      NaverMap,
      Marker,
    } = require('react-naver-maps')
    const { username } = this.state; //for save data
    const { selectedOption } = this.state; //for select box
    const { videoUrl } = this.state; //for select box
    const { videoUrl1 } = this.state; //for select box
    const { videoUrl2 } = this.state; //for select box
    const { videoUrl3 } = this.state; //for select box
    const { videoUrl4 } = this.state; //for select box
    const { videoUrl5 } = this.state; //for select box
    const { videoUrl6 } = this.state; //for select box
    const { text1 } = this.state;
    const { text2 } = this.state;
    const { text3 } = this.state;
    const { text4 } = this.state;
    const { text5 } = this.state;
    const { text6 } = this.state;

    const { selectedVideoOption } = this.state; //for select box
    const { markcolor1 } = this.state; //for select box'
    const { markcolor2 } = this.state; //for select box'
    const { markcolor3 } = this.state; //for select box'
    const { output } = this.state; //for select box

    return (
      
      <div className='container' style={{ maxWidth: 1200, padding: '5px 0' }}>
      
        <Helmet bodyAttributes={{ style: 'background-color : #0d296b' }} />
        <div className='row' style={{ marginTop: 40 }}>
          <div className='pj Title'>
            <p style={{
              color: "white"
            }}>
              It is from{' '}
              <Typical
                loop={Infinity}
                wrapper="b"
                steps={['DY 🤸‍♂️', 1500, 'and HJ 🏋️‍♀️', 1500]}
              />
            </p>
            <h3 style={{ color: "white", fontWeight: 'bold' }}>‘OpenPose’ based ‘Human Re-Identification’ system ❛‿❛</h3>
            <h3 style={{
              color: "white"
            }}>- cocoFam</h3>
          </div>
        </div>

        <div className='row' style={{ marginTop: 40 }}>
          <div className='col-6' style={{ marginTop: 40 }}>
            <ReactPlayer
              ref={this.player}
              url={videoUrl}
              playing={true}
              loop={true}
              width='100%'
              height='40%'
              controls={true}
            />
            <div className='container' style={{marginLeft:35,marginTop:40}}>
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl1}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
                <p style={{marginLeft:13,color:"white"}}>
                  {text1}
                </p>
              </div >
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl2}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
              </div>
              <p style={{color:"white"}}>
                  {text2}
                </p>
            </div>
            <div className='container' style={{marginLeft:35,marginTop:20}}>
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl3}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
                   <p style={{marginLeft:13,color:"white"}}>
                  {text3}
                </p>
              </div >
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl4}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
              </div>
              <p style={{color:"white"}}>
                  {text4}
                </p>
            </div>
            <div className='container' style={{marginLeft:35,marginTop:20}}>
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl5}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
                   <p style={{marginLeft:13,color:"white"}}>
                  {text5}
                </p>
              </div >
              <div className='row' style={{maxWidth:300, float:"left"}}>
                <ReactPlayer
                  ref={this.player}
                  url={videoUrl6}
                  playing={true}
                  loop={true}
                  width='80%'
                  height='10%'
                  controls={true}
                />
              </div>
              <p style={{color:"white"}}>
                  {text6}
                </p>
            </div>
           

            <h5 style={{ color: "white", marginTop: 20 }}></h5>
           
            <div className='column'>
         
        </div>
            <div className='run_py' style={{ marginTop: 20, marginLeft: 210 }}>
             
            </div>

          </div>
          <div className='col-6'>
            <RenderAfterNavermapsLoaded
              ncpClientId={'r7h3b0k62j'} // 자신의 네이버 계정에서 발급받은 Client ID
              error={<p style={{ color: "white" }}>Maps Load Error</p>}
              loading={<p style={{ color: "white" }}>Maps Loading...</p>}
            >
              <NaverMap
                mapDivId={'maps-getting-started-uncontrolled'} // default: react-naver-map
                style={{
                  width: '100%', // 네이버지도 가로 길이
                  height: '40vh' // 네이버지도 세로 길이
                }}

                defaultCenter={{ lat: 37.384850, lng: 126.656200 }} // 지도 초기 위치
                defaultZoom={20} // 지도 초기 확대 배율
              >

                <Circle
                  key={4}
                  center={{ x: 126.656002, y: 37.384900 }}
                  radius={2}
                  fillOpacity={markcolor3}
                  fillColor={'#FF0000'}
                  strokeColor={'red'}
                  clickable={true} // click event를 다루기 위해서는 true로 설정되어야함.
                  //        visible ={true}
                  onClick={() => {
                    alert('CAM3 Position')
                  }}
                />
                <Circle
                  key={5}
                  center={{ x: 126.656450, y: 37.384850 }}
                  radius={2}
                  fillOpacity={markcolor2}
                  fillColor={'#FF0000'}
                  strokeColor={'red'}
                  clickable={true} // click event를 다루기 위해서는 true로 설정되어야함.
                  onClick={() => {
                    alert('CAM2 Position')
                  }}
                />
                <Circle
                  key={5}
                  center={{ x: 126.656200, y: 37.384800 }}
                  radius={2}
                  fillOpacity={markcolor1}
                  fillColor={'#FF0000'}
                  strokeColor={'red'}
                  clickable={true} // click event를 다루기 위해서는 true로 설정되어야함.
                  onClick={() => {
                    alert('CAM1 Position')
                  }}
                />
                <Marker
                  key={1}
                  position={{ x: 126.656002, y: 37.384900 }}
                />
                <Marker
                  key={2}
                  position={{ x: 126.656450, y: 37.384850 }}
                  text={'3'}
                />
                <Marker
                  key={3}
                  position={{ x: 126.656200, y: 37.384800 }}
                  text={'3'}
                />
              </NaverMap>

            </RenderAfterNavermapsLoaded>
            <div className="output" style={{ marginTop: 20 }}></div>
            <div className='select_video' style={{ marginTop: 0 }}>
              <h6 style={{ color: "white" }}>Select Video</h6>
              <Select
                value={selectedVideoOption}
                onChange={this.handleVideoChange}
                options={video_options}
              />
            </div>
            <div className='select_time' style={{ marginTop: 10 }}>
              <h6 style={{ color: "white" }}>Select Time</h6>
              <Select
                value={this.state.selectedOption}
                options={frame_options}
                onChange={this.handleChange}
              />
            </div>
            <h6 style={{ color: "white" ,marginTop: 10 }}>Show Outputs </h6>
            <div>
              <textarea value={this.state.output} rows={6} cols={64}> 
              </textarea>
            </div>
            <div className='column'>
        </div>
          </div>
        </div>
      </div >
    );
  }
}

export default App;