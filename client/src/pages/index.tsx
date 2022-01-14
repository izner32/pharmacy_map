// TODO - fix fetching api, add heatmap layer
import React, { useState, useEffect } from "react";
import {
  withGoogleMap,
  withScriptjs,
  GoogleMap,
  Marker,
  InfoWindow
} from "react-google-maps";
// import * as parkData from "./data/skateboard-parks.json";
// import mapStyles from "./mapStyles";

function Map() {
  const [pharmacyList, setPharmacyList] = useState(null);

  // using escape from keyboard to make the popup go away 
  useEffect(() => {
    const listener = e => {
      if (e.key === "Escape") {
        setPharmacyList(null);
      }
    };
    window.addEventListener("keydown", listener); // keydown is for a keyboard key

    return () => {
      window.removeEventListener("keydown", listener);
    };
  }, []); // blank array means only do this once 

  /* TODO : 
    fix errors in cors policy
    add location bias
    make the result into multiple candidates
  */

  // fetching data - grab the type, it must be equal to pharmacy 
  useEffect( () => {
    const fetchDataForPharmacy = async () => {
      try {
        const res = await fetch(`https://maps.googleapis.com/maps/api/place/findplacefromtext/json?&fields=formatted_address%2Cname%2Ctypes%2Cplace_id%2Cgeometry&input=pharmacy&inputtype=textquery&key=AIzaSyDBqerYcBLd6bAM2S_GAmLejYH_xVNNa-U`);
        console.log(res);
        const data = await res.json();

        // at query above
        //&locationbias=circle%3A2000%14.1153%120.9621 
        
        console.log(data);
        // setPharmacyList(data);
        // console.log(pharmacyList.candidates[0].position);
      } catch (e) {
        console.error(e);
      }
    }
    fetchDataForPharmacy();
  },[]);

  return (
    <GoogleMap
      defaultZoom={10}
      defaultCenter={{ lat: 14.1153, lng: 120.9621}}
      //defaultOptions={{ styles: mapStyles }}
    >
      {/* for displaying result */}
      {/* {pharmacyList.candidates.map(pharmacy => (
        <Marker
          key={pharmacy.places_id}
          position={{
            lat: pharmacy.location.lat,
            lng: pharmacy.location.lng
          }}
          // onClick={() => {
          //   setSelectedPark(park);
          // }}
          // icon={{
          //   url: `/skateboarding.svg`,
          //   scaledSize: new window.google.maps.Size(25, 25)
          // }}
        />
        )) }  */}

      {/* for creating the popup */}
      {/* selectedPark && (
        <InfoWindow
          onCloseClick={() => {
            setSelectedPark(null);
          }}
          position={{
            lat: selectedPark.geometry.coordinates[1],
            lng: selectedPark.geometry.coordinates[0]
          }}
        >
          <div>
            <h2>{selectedPark.properties.NAME}</h2>
            <p>{selectedPark.properties.DESCRIPTIO}</p>
          </div>
        </InfoWindow>
        ) */}
    </GoogleMap>
  );
}

const MapWrapped = withScriptjs(withGoogleMap(Map));

export default function Home() {
  return (
    <div style={{ width: "100vw", height: "100vh" }}>
      <MapWrapped
        googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=
        AIzaSyDBqerYcBLd6bAM2S_GAmLejYH_xVNNa-U`
        //${process.env.REACT_APP_GOOGLE_KEY}
        }
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `100%` }} />}
        mapElement={<div style={{ height: `100%` }} />}
      />
    </div>
  );
}
