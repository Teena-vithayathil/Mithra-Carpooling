<template>
  <div id="AdminPage" style="background-color: #fad3a5; display: flex; flex-direction: column; height: 150vh;">
    <header style="padding: 20px; background-color: white; display: flex; justify-content: space-between; align-items: center;">
      <h1 style="color:#fb0f72;">Mithra Carpooling</h1>
      <p style="cursor: pointer; margin-left:850px;" @click="driving_license" ><u>Driving license</u></p>
      <p style="cursor: pointer; " @click="carpool" ><u>Carpools created</u></p>
      <p style="cursor: pointer;" @click="signout" ><u>Sign out</u></p>
      <p style="cursor: pointer;" @click="aboutUs"><u>About Us</u></p>
    </header>
    <p></p>
    <h2>ID PROOF VERIFICATION</h2>
    <div v-for="user in result" v-bind:key="user.id" class="user-box">
      <div class="user-details">
        <p><strong>Name: </strong>{{ user.username }}</p>
        <p><strong>Age: </strong>{{ user.age }}</p>
        <div v-if="user.id_proof">
          <a :href="user.id_proof" target="_blank">View ID Proof</a>
        </div>
      </div>
      <div class="user-actions">
        <button class="accept-btn" @click="acceptUsers(user)">Accept</button>
        <button class="reject-btn" @click="rejectUsers(user)">Reject</button>
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
      result: [],
    };
  },
  methods: {
    acceptUsers(user) {
      axios.post("http://127.0.0.1:8000/accept-verification/", { user_id: user.id })
        .then(response => {
          console.log(response.data);
          this.fetchUsers();
        })
        .catch(error => {
          console.error('Error accepting users:', error);
        });
    },
    rejectUsers(user) {
      axios.post("http://127.0.0.1:8000/reject-verification/", { user_id: user.id })
        .then(response => {
          console.log(response.data);
          this.fetchUsers();
        })
        .catch(error => {
          console.error('Error rejecting users:', error);
        });
    },
    fetchUsers() {
      axios.post("http://127.0.0.1:8000/verification/")
        .then(({ data }) => {
          console.log(data);
          this.result = data;
        })
        .catch(error => {
          console.error('Error fetching users:', error);
        });
    },
    signout()
      {
        this.$router.push({ name: 'StPage' });
      },
    carpool()
    {
      this.$router.push({ name: 'CarpoolsCreated' });
    },
    aboutUs() {
        this.$router.push({ name: 'AboutUs' });
    },
    driving_license(){
      this.$router.push({ name: 'DrivingLicense' });
    }
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>

<style>
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
.user-box {
  background-color: white;
  margin-bottom: 20px;
  margin-left:30px;
  display: flex;
  justify-content: space-between;
  padding: 20px;
  width: 1100px;
}

.user-actions {
  display: flex;
}

.accept-btn {
  background-color: green;
  color: white;
  margin-right: 10px;
}

.reject-btn {
  background-color: red;
  color: white;
}
</style>
