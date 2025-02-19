<script lang="ts">
    async function create_user() {
        const response = fetch("http://127.0.0.1:8000/users/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: "John Doe",
                email: "johndoe@gmail.com",
                frequency: new Date().getMilliseconds(),
                categories: ["news"],
            }),
        });

        console.log(await response);
    }

    async function get_users() {
        const response = await fetch("http://127.0.0.1:8000/users", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        });

        return await response.json();
    }
</script>

<button on:click={create_user}>Create User</button>

{#await get_users()}
    <p>Loading...</p>
{:then response}
    {#each response as user}
        <p>{user.name}</p>
        <p>{user.email}</p>
        <p>{user.frequency}</p>
        {#each user.categories as category}
            <p>{category}</p>
        {/each}
    {/each}
{:catch error}
    <p>{error}</p>
{/await}
