This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

# Re-ID_with_Openpose Data
### with React
#### We applied the proposed re-identification algorithm system to images acquired from CCTV to evaluate its performance with the results and confirmed that it is possible to re-identify it with Highly accuracy without face information.

The ability to re-identify the same person through CCTV is very critical in tracking down criminals. 
The existing technology of re-identification through CCTV requires human face information which can guarantee the accuracy of human re-identification.  
However, this face recognition technology does not work properly because it cannot see the face intuitively through CCTV in the current situation where everyone is wearing a mask due to the COVID19 incident. 
These results can lead to inappropriate re-identification results and increased crime rates. 
Therefore, this paper proposes a re-identification algorithm by combining the joint ratio data with clothing color data, without human face information, which can be applied to human re-identification with masks or disguises. 
OpenPose is utilized to extract the joint ratio data and the Color Histogram data. 
We applied the proposed re-identification algorithm system to images acquired from CCTV to evaluate its performance with the results and confirmed that it is possible to re-identify it with Highly accuracy without face information.



## << Re-ID System FlowChart >>

![4](https://user-images.githubusercontent.com/54773137/104900426-67cc4d00-59bf-11eb-8225-75f48cc974bc.jpg)

![5](https://user-images.githubusercontent.com/54773137/104900469-6f8bf180-59bf-11eb-8a8b-ae3101145a77.jpg)



## << SW,HW Spec >>

![6](https://user-images.githubusercontent.com/54773137/104900481-731f7880-59bf-11eb-8c62-ee5d747ce8bb.jpg)



## << Re-ID System GUI >>

#### 1) FIRST PAGE
<img width="1677" alt="스크린샷 2021-01-18 오후 6 05 19" src="https://user-images.githubusercontent.com/54773137/104894610-42881080-59b8-11eb-9a2f-49b437d4abdd.png">

#### 2) FIND A with customized Re-ID Algorithm result
<img width="1677" alt="스크린샷 2021-01-18 오후 6 06 12" src="https://user-images.githubusercontent.com/54773137/104894623-487df180-59b8-11eb-9057-f53c64306b2e.png">

#### 3) FIND B with customized Re-ID Algorithm result
<img width="1677" alt="스크린샷 2021-01-18 오후 6 06 36" src="https://user-images.githubusercontent.com/54773137/104894629-4ae04b80-59b8-11eb-8ee7-ef84b03bbc74.png">

#### 4) FIND C with customized Re-ID Algorithm result
<img width="1677" alt="스크린샷 2021-01-18 오후 6 07 15" src="https://user-images.githubusercontent.com/54773137/104894641-4e73d280-59b8-11eb-9ff5-f69f77a750b5.png">

## Available Scripts ABOUT react app

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
