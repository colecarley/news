<script>
    import Button from "../../components/button.svelte";
    import Center from "../../components/center.svelte";
    import Input from "../../components/input.svelte";
    import Page from "../../components/page.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Page>
    <Center>
        <Squeeze>
            <Center>
                <h1>Sign Up!</h1>
                <div class="flex flex-col w-1/2 gap-2">
                    <Input type="text" label="First Name" placeholder="John" />
                    <Input type="text" label="Last Name" placeholder="Doe" />
                    <Input
                        type="text"
                        label="Email"
                        placeholder="johndoe@email.com"
                    />

                    <div class="w-fit">
                        <Button onclick={(e) => {}}>Choose Categories</Button>
                    </div>
                </div>
            </Center>
        </Squeeze>
    </Center>
</Page>
