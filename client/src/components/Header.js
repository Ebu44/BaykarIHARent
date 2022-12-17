function Header() {
    return (
        <>
            <div className="flex dark:bg-slate-700 justify-between">
                <div className="text-3xl font-bold m-8">
                    LOGO
                </div>
                <div>
                    <ul className="flex">
                        <li className="flex hover:bg-violet-600 active:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-300 m-8 px-8 py-3 rounded-full bg-violet-400">
                            <a href="#">UAV</a>
                        </li>
                        <li className="flex hover:bg-violet-600 active:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-300 m-8 px-8 py-3 rounded-full bg-violet-400">
                            <a href="#">Brand</a>
                        </li>
                        <li className="flex hover:bg-violet-600 active:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-300 m-8 px-8 py-3 rounded-full bg-violet-400">
                            <a href="#">Model</a>
                        </li>
                    </ul>
                </div>
            </div>
        </>
    );
}

export default Header;
