<template>
  <div id="CreateCarpoolPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 100vh;">
  <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
    <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
    <div class="header-links">
    <p style="cursor: pointer;margin-right: 20px;" @click="aboutUs"><u>About Us</u></p>
    <p style="cursor: pointer; margin-right: 20px;" @click="signOut"><u>Sign Out</u></p>
    <p style="cursor: pointer;" @click="goToMyProfile"><u>My Profile</u></p>
  </div>
  </header>
  <div>
    <p></p>
  <div class="container" style="flex-grow: 1; display: flex; justify-content: center; margin-top:50px; align-items: center;">
    <div class="form-container" style="padding: 20px; border: 1px solid black; border-radius: 10px; background-color: rgba(255, 255, 255, 0.5); max-width: 600px; height:350px;">
      <div style="text-align: center; margin-bottom: 20px;">
        <h2>Upload ID Proof</h2>
        <label for="idProof" class="custom-file-upload button-style" style="margin-left:10px; margin-bottom:30px; ">
          Upload ID Proof
        </label>
        <input id="idProof" type="file" @change="handleIdProofChange" style="display:none;">
      </div>
      <div style="text-align: center; margin-bottom: 20px;">
        <h2>Upload Driving License</h2>
        <label for="drivingLicense" class="custom-file-upload button-style" style="margin-left:10px; margin-bottom:30px; ">
          Upload ID Proof
        </label>
        <input id="drivingLicense" type="file" @change="handleDrivingLicenseChange" style="display:none;">
      </div>
      <button @click="uploadFiles" style="width: 100%; background-color:pink; width:200px; height:40px; border-radius: 20px; font-weight:bold">Upload</button>
    </div>
  </div>
</div>
</div>
  <footer class="footerComponent">
    <p>&copy; 2024 Mithra Carpooling. All rights reserved.</p>
  </footer>
</template>

<script>
import axios from 'axios';

export default {
data() {
  return {
    idProofFile: null,
    drivingLicenseFile: null,
  }
},
methods: {
  handleIdProofChange(event) {
    this.idProofFile = event.target.files[0];
  },
  handleDrivingLicenseChange(event) {
    this.drivingLicenseFile = event.target.files[0];
  },
  async uploadFiles() {

    const formData = new FormData();
    formData.append('id_proof', this.idProofFile);
    formData.append('driving_license', this.drivingLicenseFile);

    try {
      const response = await axios.post('http://127.0.0.1:8000/Signup/Files-upload/', formData);

      const data = response.data;

      if (data.message === 'proof upload complete') {
        // Redirect to homepage
        this.$router.push('/ProfileNotVerified');
      } else {
        // Handle other cases
        console.error('Upload failed');
      }
    } catch (error) {
      console.error('Error uploading files:', error);
    }
  },
  aboutUs() {
    this.$router.push({ name: "AboutUs" });
  },
  signOut() {
    this.$router.push({ name: "StPage" });
  },
  goToMyProfile() {
    this.$router.push({ name: "YourProfile" });
  }
}
}
</script>
<style>
#FileUploadPage {
display: flex;
flex-direction: column;
height: 100vh;
}

.container {
flex-grow: 1;
}

.form-container {
padding: 20px;
border: 1px solid black;
border-radius: 10px;
background-color: white;
}

button {
display: block;
margin: 0 auto;
margin-top: 20px;
}

input[type="file"] {
margin: 0 auto;
display: block;
margin-bottom: 20px;
}
.footerComponent {
background: linear-gradient(90deg, #fb0f72, #f9a84a);
padding: 20px;
text-align: center;
color: white;
}
.header-links {
  display: flex;
  align-items: center;
}
.button-style {
  background-color: orange;
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  cursor: pointer;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
