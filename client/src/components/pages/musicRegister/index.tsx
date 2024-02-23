import { useState } from "react";
import { MusicRegisterLayout } from "./layout";
import { Data } from "../../parts/searchResult";
import { useNavigate } from "react-router-dom";

export const MusicRegister = () => {
  const [searchResult, setSearchResult] = useState<Data[]>([]);
  const navigate = useNavigate();

  const getMusic = async (searchWord: string) => {
    const res = await fetch(
      `https://soundsynapse.onrender.com/artist/${searchWord}`,
      {
        method: "GET",
        mode: "cors",
      }
    );
    const result = await res.json();
    const resultItems: any = result;
    console.log(result);
    return resultItems;
  };

  const onSearch = async (searchWord: string) => {
    const searchResult = await getMusic(searchWord);
    if (!searchResult) return;
    setSearchResult(searchResult);
  };

  return (
    <MusicRegisterLayout
      onClickNextButton={(selectedMusic) => {
        navigate("/result");
      }}
      onClickSearchButton={async (value) => await onSearch(value)}
      searchResult={searchResult}
    />
  );
};
