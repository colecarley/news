<script lang="ts">
    export let onclick: (e: Event) => void;
</script>

<button {onclick} class="font-bold rounded-full bg-gray-300 p-2 px-4">
    <slot></slot>
</button>
