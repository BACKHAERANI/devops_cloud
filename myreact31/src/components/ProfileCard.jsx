import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({
  changePage,
  profileImage,
  name,
  role,
  facebook_url,
  email,
}) {
  return (
    <div>
      <section>
        <nav className="menu">
          <a href="#">
            <FontAwesomeIcon icon={faBars} />
          </a>
          <a href="#">
            <FontAwesomeIcon icon={faStickyNote} />
          </a>
        </nav>
        <article className="profile">
          <img src={profileImage} />
          <h1>{name}</h1>
          <h2>{role}</h2>
          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faFacebook} className="icon" />
            <span>
              <a href="#">{facebook_url}</a>{" "}
            </span>
          </li>
          <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li>
        </ul>
        <nav class="others">
          <a onClick={() => changePage("해란")}></a>
          <a onClick={() => changePage("찬들")}></a>
          <a onClick={() => changePage("유림")}></a>
          <a onClick={() => changePage("예린")}></a>
          <a onClick={() => changePage("진아")}></a>
          <a onClick={() => changePage("은지")}></a>
        </nav>
      </section>
    </div>
  );
}
export default ProfileCard;
