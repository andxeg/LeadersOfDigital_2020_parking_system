import React from 'react';
import {
  StyleSheet,
  View,
  Text,
  Alert,
  Button,
  TouchableOpacity,
  TextInput,
} from 'react-native';
import MapView from 'react-native-maps';
import { Icon, Input } from 'react-native-elements'
import Marker from './components/Marker.js'

const MAP_VIEW = 'map';
const MENU_VIEW = 'menu';
const CODE_VIEW = 'code';
const FEEDBACK_VIEW = 'feedback';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeView: MAP_VIEW,
      region: {
        latitude: 55.751244,
        longitude: 37.618423,
        latitudeDelta: 0.5,
        longitudeDelta: 0.5,
      },
      marks: [
      //   { coordinate: {
      //   latitude: 55.751244,
      //   longitude: 37.618423,
      // },
      // free: 5,
      // total: 55
      // }
    ],
    };
  }

  componentDidMount() {
    fetch('https://run.mocky.io/v3/9f07e3a7-f65a-4942-b272-afff80ef8712')
    .then((resp) => resp.json())
    .then(data => {
      // console.log("data", data); // DEBUG
       this.setState({ marks: data });
    }).catch(err => {
      // Error 🙁
    });
  }

  onSettingPress = () => {
    if (this.state.activeView == MAP_VIEW) {
      this.setState({ activeView: MENU_VIEW });
    } else {
      this.setState({ activeView: MAP_VIEW });
    }
  }

  onAddKeyPress = () => {
    // Alert.alert("Asd")
  }

  onTechSupportPress = () => {
    // Alert.alert("Asd")
  }
  
  render() {
    switch (this.state.activeView) {
      case MAP_VIEW:
        return (
          <View style={styles.container}>
            <MapView style={styles.map} initialRegion={this.state.region}>
              {this.state.marks.map((marker, i) => {
                // console.log("marker", marker)
                return (<Marker key={i} mark={marker.coordinate} free={marker.free} total={marker.total} />)
              })}
              {/* <Marker coordinate={this.state.mark} /> */}
              {/* <Marker mark={this.state.mark} num={5} /> */}
            </MapView>
            <TouchableOpacity style={styles.settingButton} onPress={this.onSettingPress} >
              <Icon name='bars' type='font-awesome-5' size={35} />
            </TouchableOpacity>
          </View>
        );

      case MENU_VIEW:
        return (
          <View style={styles.container}>
            <View style={styles.menuContainer}>
              <View style={styles.menuButton}>
                <Button
                  title="Ввести ключ доступа"
                  onPress={() => {
                    this.setState({ activeView: CODE_VIEW });
                  }}
                />
              </View>
              <View style={styles.menuButton}>
                <Button
                  title="Обратиться в поддержку"
                  onPress={() => {
                    this.setState({ activeView: FEEDBACK_VIEW });
                  }}
                />
              </View>
            </View>
            <TouchableOpacity style={styles.settingButton} onPress={this.onSettingPress} >
              <Icon name='arrow-left' type='font-awesome-5' size={35} />
            </TouchableOpacity>
          </View>
        );

      case CODE_VIEW:
        return (
          <View style={styles.container}>
            <View style={styles.feedbackContainer}>
              <View style={styles.feedbackText}>
                {/* <TextInput
                  editable
                  maxLength={40}
                  style={{backgroundColor:"#fff", marginBottom: 25}}
                /> */}
                <Input
                  placeholder='  Вставьте код сюда'
                  leftIcon={
                    <Icon
                      name='key'
                      type='font-awesome-5'
                      size={20}
                      color="gray"
                    />
                  }
                />
                <Button
                  title="Отправить"
                  onPress={() => {
                    this.setState({ activeView: MENU_VIEW });
                    Alert.alert("Код доступа успешно добавлен!")
                  }}
                />
              </View>
            </View>
            <TouchableOpacity style={styles.settingButton} onPress={()=>{
              this.setState({ activeView: MENU_VIEW });
            }} >
              <Icon name='arrow-left' type='font-awesome-5' size={35} />
            </TouchableOpacity>
          </View>
        );

      case FEEDBACK_VIEW:
        return (
          <View style={styles.container}>
            <View style={styles.feedbackContainer}>
              <View style={styles.feedbackText}>
                <TextInput
                  multiline
                  numberOfLines={20}
                  editable
                  maxLength={40}
                  style={{backgroundColor:"#fff", marginBottom: 25}}
                />
                <Button
                  title="Отправить"
                  onPress={() => {
                    this.setState({ activeView: MENU_VIEW });
                    Alert.alert("Ваше обращение успешно отправлено!")
                  }}
                />
              </View>
            </View>
            <TouchableOpacity style={styles.settingButton} onPress={()=>{
              this.setState({ activeView: MENU_VIEW });
            }} >
              <Icon name='arrow-left' type='font-awesome-5' size={35} />
            </TouchableOpacity>
          </View>
        );
    
      default:
        return (
          <View>
            <Text>Sorry, something went wrong :(</Text>
          </View>
        );
    }
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'flex-end',
    justifyContent: 'flex-end',
    backgroundColor: '#ddd',
  },
  menuContainer: {
    flex: 1,
    backfaceVisibility: "visible",
    // backgroundColor: "#f0f", // DEBUG 
    alignSelf: 'center',
    paddingTop: "10%",
    // alignItems: 'center',
    justifyContent: 'center',
  },
  feedbackContainer: {
    flex: 1,
    backfaceVisibility: "visible",
    // backgroundColor: "#f0f", // DEBUG 
    alignSelf: 'center',
    paddingTop: "10%",
    // alignItems: 'center',
    justifyContent: 'flex-start',
  },
  map: {
    ...StyleSheet.absoluteFillObject,
  },
  button: {
    margin: 20,
  },
  settingButton: {
    margin: 30,
    borderWidth:2,
    borderColor:'rgba(0,0,0,0.2)',
    alignItems:'center',
    justifyContent:'center',
    width:60,
    height:60,
    backgroundColor:'rgba(200,200,200,0.65)',
    borderRadius:50,
  },
  menuButton: {
    margin: 15,
    width: 250,
  },
  feedbackText: {
    margin: 30,
    width: 275,
  },
});

export default App;