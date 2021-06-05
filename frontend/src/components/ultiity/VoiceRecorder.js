import AudioReactRecorder from 'audio-react-recorder'

const VoiceRecorder = ({recordState, onStop, start, stop, mediaData}) => {
    return (
        <div className="recorder">
          <h3>Option 1: Record</h3>
          <AudioReactRecorder state={recordState} onStop={onStop} />
          <audio
            id='audio'
            controls
            src={mediaData ? mediaData.url : null}
          ></audio>
          <div>
            <button onClick={start}>Start</button>
            <button onClick={stop}>Stop</button>
          </div>
        </div>
    )
}

export default VoiceRecorder
