import { useState, useEffect } from "react";
import Axios from "axios";

function PageProfile() {
  const [profileList, setProfileList] = useState([]);
  const [checkError, setCheckError] = useState(null);
  const [query, setQuery] = useState("");

  const handleRefresh = () => {
    setCheckError(null);
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        setProfileList(
          response.data.map((profile) => ({
            name: profile.name,
            role: profile.role,
            mbti: profile.mbti,
            unique: profile.unique_id,
            profileimageurl: profile.profile_image_url,
            instagramurl: profile.instagram_url,
          }))
        );
      })
      .catch((error) => {
        setCheckError(error);
      });
  };

  useEffect(() => {
    handleRefresh();
  }, []);

  const handleChange = (e) => {
    const value = e.target.value;
    console.log(value);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      console.log("ENTER");
      const value = e.target.value;
      setQuery(value);
    }
  };

  return (
    <div>
      <h2>PageProfile</h2>

      <button onClick={() => setProfileList([])}>clear</button>

      <button onClick={handleRefresh}>새로고침</button>

      <input
        type="text"
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onKeyPress={handleKeyPress}
      />
      {profileList.length == 0 && !checkError && (
        <h3>등록된 프로필이 없습니다.</h3>
      )}

      {checkError && <h3>오류가 발생했습니다. 잠시후 다시 시도해주세요.</h3>}

      {profileList
        .filter((member) => {
          return (
            member.name.includes(query) ||
            member.role.includes(query) ||
            member.mbti.includes(query)
          );
        })
        .map((member) => {
          return (
            <>
              <h3>
                [{member.unique}]{member.name}
              </h3>
              <ul>
                <img src={member.profileimageurl} />
                <li>{member.role}</li>
                <li>{member.instagramurl}</li>
                <li>{member.mbti}</li>
              </ul>
            </>
          );
        })}
    </div>
  );
}

export default PageProfile;
