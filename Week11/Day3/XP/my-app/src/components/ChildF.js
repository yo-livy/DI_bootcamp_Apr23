import { useEffect } from "react";

const ChildF = () => {

    useEffect(() => {
        console.log('Some text Child');
        return () => {
            console.log('Unmount Child');
        }
    }, [])


    return (
        <div>
            <h1>Hello world!</h1>
        </div>
    )
}

export default ChildF;