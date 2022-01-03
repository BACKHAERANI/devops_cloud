import "./ProfileCard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faBars,
  faEnvelope,
  faStickyNote,
} from "@fortawesome/free-solid-svg-icons";
import { faInstagram } from "@fortawesome/free-brands-svg-icons";

function ProfileCard({
  mbti,
  instagram_url,
  profile_image_url,
  name,
  role,
  children,
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
          <img src={profile_image_url} />
          <h1>{name}</h1>
          <h2>{role}</h2>
          <h2>{mbti}</h2>
          <a href="#" className="btnView">
            VIEW MORE
          </a>
        </article>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faInstagram} className="icon" />
            <span>
              <a href="#">{instagram_url}</a>{" "}
            </span>
          </li>
        </ul>
        <nav className="others">{children}</nav>
      </section>
    </div>
  );
}
export default ProfileCard;
