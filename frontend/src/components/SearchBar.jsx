import { React, useState } from "react";
import axios from "axios";

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import TextField from '@mui/material/TextField'

import styles from "../components/SearchBar.module.css";
import API_URL from "../Config";

const SearchBar = () => {
    const [query, setQuery] = useState('');
    const [queryResults, setQueryResults] = useState([]);

    const handleChange = (event) => {
        let query = event.target.value
        setQuery(query);
        // console.log(query);

        let url = `${API_URL}/profiles/query/?query=${query}`;
        url = encodeURI(url);
        // console.log(url);
        axios.get(url).then((response) => {
            setQueryResults(response.data);
        });
    }

    return (
        <div className={styles.container}>
            <TextField
                id="outlined-basic"
                label="Search User"
                variant="outlined"
                sx = {{width: '60%'}}
                onChange={handleChange}
            />
            <List>
                {queryResults.map((result) => (
                    <ListItem
                        key={result.id}
                    >
                        <ListItemText
                            primaryTypographyProps={{fontSize: '18px'}}
                            primary={`${result.first_name} ${result.last_name}`} />
                    </ListItem>
                ))}
            </List>
        </div>
    );
}

export default SearchBar