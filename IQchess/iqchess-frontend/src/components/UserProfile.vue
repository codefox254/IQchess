<template>
  <div class="user-profile">
    <h2>User Profile</h2>
    <div class="profile-details">
      <p><strong>Username:</strong> {{ user.username }}</p>
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Rating:</strong> {{ user.rating }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  props: {
    user: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped>
.user-profile {
  margin-top: 20px;
}

.profile-details {
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>