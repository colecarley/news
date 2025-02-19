<script lang="ts">
    function create_user() {
        fetch("http://127.0.0.1:8000/users/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: "John Doe",
                email: "johndoe@gmail.com",
                frequency: new Date().getMilliseconds(),
                category: ["news"],
            }),
        });
    }
</script>

<button on:click={create_user}>Create User</button>
