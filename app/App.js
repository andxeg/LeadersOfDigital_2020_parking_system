import React, { Component } from 'react';
import {
  StyleSheet,
  View,
  Text,
  Alert,
  Button,
  Dimensions,
  TouchableOpacity,
} from 'react-native';
import MapView, {TouchableHighlight} from 'react-native-maps';
import { showLocation } from 'react-native-map-link'

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
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
      console.log("data", data);
       this.setState({ marks: data });
    }).catch(err => {
      // Error 🙁
    });
  }
  
  render() {
    return (
      <View style={styles.container}>
        <MapView style={styles.map} initialRegion={this.state.region}>
          {this.state.marks.map((marker, i) => {
            console.log("marker", marker)
            return (<Marker key={i} mark={marker.coordinate} free={marker.free} total={marker.total} />)
          })}
          {/* <Marker coordinate={this.state.mark} /> */}
          {/* <Marker mark={this.state.mark} num={5} /> */}
        </MapView>
      </View>
    );
  }
}

class Marker extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      mark: props.mark,
      free: props.free,
      total: props.total
    }
  }
  render() {
    var style = styles.circleRed;
    if (this.state.free/this.state.total < 0.3) {
      style = styles.circleRed
    } else if (this.state.free/this.state.total < 0.7) {
      style = styles.circleYellow
    } else {
      style = styles.circleGreen
    }
    return (
    <MapView.Marker  coordinate={this.state.mark} onPress={() => {
      console.log("this", this)
      showLocation({
        latitude: this.state.mark.latitude,
        longitude: this.state.mark.longitude,
      })
    }}>
          <View style={style}>
            <Text style={styles.pinText}>{this.state.free}/{this.state.total}</Text>
          </View>
    </MapView.Marker>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  map: {
    ...StyleSheet.absoluteFillObject,
  },
  button: {
    margin: 20,
  },
  circleRed: {
    width: 60,
    height: 30,
    borderRadius: 30 / 2,
    backgroundColor: 'red',
  },
  circleYellow: {
    width: 60,
    height: 30,
    borderRadius: 30 / 2,
    backgroundColor: '#edbf37',
  },
  circleGreen: {
    width: 60,
    height: 30,
    borderRadius: 30 / 2,
    backgroundColor: 'green',
  },
  pinText: {
    color: 'white',
    fontWeight: 'bold',
    textAlign: 'center',
    fontSize: 20,
    marginBottom: 10,
  },
});

export default App;