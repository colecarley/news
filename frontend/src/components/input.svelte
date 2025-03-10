<script lang="ts">
    export let type: string;
    export let placeholder: string;
    export let label: string;
</script>

<div class="flex flex-col gap-1">
    <label for={label}>{label}</label>
    <input
        id={label}
        {type}
        {placeholder}
        class="outline-2 outline-gray-200 rounded-lg p-2 bg-white"
    />
</div>
