<script lang="ts">
    import { TestDatabase, type Database } from "$lib/db";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";
    import Summary from "../../components/summary.svelte";
    import Page from "../../components/page.svelte";
    import Link from "../../components/link.svelte";

    const db: Database = new TestDatabase();
</script>

<Page>
    <Center>
        <Squeeze>
            <Center>
                <div class="flex flex-col gap-6">
                    <h1>Examples</h1>
                    <div class="flex flex-col justify-between gap-6">
                        {#await db.getLatestSummarizations() then summarizations}
                            {#each summarizations as summary}
                                <Summary {summary} />
                            {/each}
                        {/await}
                    </div>

                    <Center>
                        <p>Want your own newsletter?</p>
                        <Link style="button" href="sign-up">Sign Up</Link>
                    </Center>
                </div>
            </Center>
        </Squeeze>
    </Center>
</Page>
