const FetchPost = () => {

    const postData = async () => {
        const dataToSend = {
            key1: 'myusername',
            email: 'mymail@gmail.com',
            name: 'Isaac',
            lastname: 'Doe',
            age: 27
        }
        try {
            const res = await fetch('https://webhook.site/cb860ee2-7ba7-43da-a67c-5ee6c6ff65a6', { 
                method: 'POST',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(dataToSend)
            })

            console.log(res);
        } catch (error) {
            console.log(error)
        }
    }

    return (
        <div>
            <h1>Fetch POST</h1>
            <button onClick={postData}>Get Response</button>  
        </div>

    )
}

export default FetchPost;