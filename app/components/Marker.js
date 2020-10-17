import React from 'react';
import {
  StyleSheet,
  View,
  Text,
} from 'react-native';
import MapView from 'react-native-maps';
import { showLocation } from 'react-native-map-link'

export default class Marker extends React.Component {
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
      // console.log("this", this)
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
